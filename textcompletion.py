from flask import Flask, render_template, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
import openai

class TextCompletionForm(FlaskForm):
    text = TextAreaField('Enter your text:', validators=[validators.InputRequired()])


class TextComplete():
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.route()

    def route(self):
        self.app.route('/text-completion', methods=['GET', 'POST'])(self.text_completion)

    def text_completion(self):
        self.form = TextCompletionForm(request.form)
        suggestion = None
        self.cursor = self.connection.cursor()
        email = session.get('email')
        if self.form.validate_on_submit():
            text = self.form.text.data
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"I want you to assume the role as a brilliant writting assistant who can complete the unfinished sentence, you have to finish the following text in full with only the new predictions based on the original meaning and must not have my given text. Please do not tell me who you are:\n{text}",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            suggestion = f"{text} {response.choices[0].text.strip()}"
            sql = "INSERT INTO textcomplete (user_id, text, answer) SELECT id, %s, %s FROM users WHERE email = %s"
            values = (text, suggestion, email)
            self.cursor.execute(sql, values)
            self.connection.commit()

            # Retrieve data from the database
        sql = "SELECT text, answer FROM textcomplete WHERE user_id IN (SELECT id FROM users WHERE email = %s)"
        self.cursor.execute(sql, (email,))
        results = self.cursor.fetchall()
        history = [{'text': result[0], 'answer': result[1]} for result in results]
    
        return render_template("text_completion.html", form=self.form, suggestion=suggestion, current_user=session.get('current_user'), history=history)
