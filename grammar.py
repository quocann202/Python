from flask import Flask, render_template, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
import openai
from builtins import zip
import re
import requests
import random

class GrammarForm(FlaskForm):
    text = TextAreaField('Enter your text:', validators=[validators.InputRequired()])


class GrammarError():
    def __init__(self, text):
        self.text = text
        self.grammar_errors = []
        
        prompt = f"Please indicate each word in the following text that has incorrect grammar:\n{text}"
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        
        for choice in response.choices:
            errors = ' '.join(word.strip() for word in choice.text.strip().split())
            self.grammar_errors.append(errors)

class CorrectError():
    def __init__(self, text):
        self.corrected_errors = []
        grammar_error = GrammarError(text)
        grammar_errors = grammar_error.grammar_errors
        
        for error in grammar_errors:
            prompt = f"Please correct any words {error} in the following text to have correct grammar, indicate only the word you corrected and nothing else."
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            for choice in response.choices:
                corrected_word = ' '.join(word.strip() for word in choice.text.strip().split())
                self.corrected_errors.append(corrected_word)
                break

class GrammarCheck():
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.route()
    def route(self):
        self.app.route('/grammar-check', methods=['GET', 'POST'])(self.grammar_check)
    def grammar_check(self):
        self.form = GrammarForm(request.form)
        error = None
        suggestion = None
        grammar_errors = None
        highlighted = "" 
        new = []
        self.cursor = self.connection.cursor()
        email = session.get('email')
        if self.form.validate_on_submit():
            text = self.form.text.data
            grammar_error = GrammarError(text)
            grammar_errors = grammar_error.grammar_errors
            prompt = f"I want you to rewrite all the text with the correct grammar and no paraphrase or completion text:\n{text}"
            
            if not (text[0].isupper() and text[-1] == '.'):
                error = "You must have the first letter in uppercase and a period at the end!"
                return render_template('grammar_check.html', form=self.form, suggestion=suggestion, error=error, current_user=session.get('current_user'))
            
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            words = [re.sub('[,".]', '', w) for w in text.split()]
        
            suggestion = response.choices[0].text.strip()
            highlighted = text

            for word in words:
                for errors in grammar_errors:
                    error_split = [re.sub('[,".]', '', w) for w in errors.split()]
                    if word in error_split:
                        highlighted = highlighted.replace(word, f"<mark>{word}</mark>")
                        break
        
            correct = CorrectError(text)
            corrected = correct.corrected_errors
            corrected_errors = [re.sub('[,".]', '', w) for w in corrected]

            for errors, correction in zip(grammar_errors, corrected_errors):
                error_words = re.findall(r'\b\w+\b', errors)
                corrected_words = re.findall(r'\b\w+\b', correction)
                modified_pairs = []
                
                for error_word, corrected_word in zip(error_words, corrected_words):
                    modified_pair = f"<a style='color:red'>{error_word}</a>  ➻  <a style='color:green'>{corrected_word}</a>"
                    modified_pairs.append(modified_pair)
                
                new.extend(modified_pairs)
            sql = "INSERT INTO grammar (user_id, text, answer) SELECT id, %s, %s FROM users WHERE email = %s"
            values = (text, suggestion, email)
            self.cursor.execute(sql, values)
            self.connection.commit()

            # Retrieve data from the database
        sql = "SELECT text, answer FROM grammar WHERE user_id IN (SELECT id FROM users WHERE email = %s)"
        self.cursor.execute(sql, (email,))
        results = self.cursor.fetchall()
        history = [{'text': result[0], 'answer': result[1]} for result in results]
    
        return render_template("grammar_check.html", form=self.form, suggestion=suggestion, error=error, highlighted=highlighted, new=new, current_user=session.get('current_user'), history=history)
