from flask import Flask, render_template, request, session, redirect    
from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
import openai
from googlesearch import search
import time

class PlagiarismForm(FlaskForm):
    text = TextAreaField('Enter your text:', validators=[validators.InputRequired()])

class PlagiarismCheck():
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.route()

    def route(self):
        self.app.route('/plagiarism', methods=['GET', 'POST'])(self.plagiarism)

    def searchDocument(self, text):
        link_result = None
        search_results = search(text, num=10)
        return search_results

    def similarityPercentage(self, text, document):
        input_tokens = set(text.split())
        document_tokens = set(document.split())
        similarity = len(input_tokens.intersection(document_tokens)) / len(input_tokens.union(document_tokens))
        similarity_percentage = similarity * 100
        return similarity_percentage

    def plagiarism(self):
        self.form = PlagiarismForm(request.form)
        self.cursor = self.connection.cursor()
        email = session.get('email')
        suggestion = []
        check_result = []
        error = None
        total = 0  # Initialize total similarity as 0
        count = 0  # Initialize count of documents as 0
        if self.form.validate_on_submit():
            text = self.form.text.data
            if not (text[0].isupper() and text[-1] == '.'):
                error = "You must have the first letter in uppercase and a dot at the end!"
                return render_template('plagiarism.html', form=self.form, suggestion=suggestion, error=error, current_user=session.get('current_user'))
            else:
                search_results = self.searchDocument(text)
                for result in search_results:
                    document = openai.completions.create(
                        model="gpt-3.5-turbo-instruct",
                        prompt=f"Please compare the text '{text}' with the text from url '{result}'",
                        max_tokens=1024,
                        stop=None,
                        temperature=0.6)["choices"][0]["text"].strip()
                    similarity = self.similarityPercentage(text, document)
                    check_result.append((result, similarity))
                    total += similarity
                    count += 1
                    time.sleep(2)
                check_result.sort(key=lambda x: x[1], reverse=True)
                suggestion.append(check_result)
                if count > 0:
                    average_similarity = total / count 
                else:
                    average_similarity = 0
                # sql = "INSERT INTO plagiarism (user_id, text, answer) SELECT id, %s, %s FROM users WHERE email = %s"
                # values = (text, suggestion, email)
                # self.cursor.execute(sql, values)
                # self.connection.commit()
                return render_template('plagiarism.html', form=self.form, suggestion=suggestion, error=error, current_user=session.get('current_user'), total=average_similarity)

        sql = "SELECT text, answer FROM plagiarism WHERE user_id IN (SELECT id FROM users WHERE email = %s)"
        self.cursor.execute(sql, (email,))
        results = self.cursor.fetchall()
        history = [{'text': result[0], 'answer': result[1]} for result in results]
    
        return render_template('plagiarism.html', form=self.form, suggestion=suggestion, error=error, current_user=session.get('current_user'), total=total, history=history)

