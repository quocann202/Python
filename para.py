from flask import Flask, render_template, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
import openai

class ParaForm(FlaskForm):
    text = TextAreaField('Enter your text:', validators=[validators.InputRequired()])

class ParaPhrase:
    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.route()

    def route(self):
        self.app.route('/paraphrase', methods=['GET', 'POST'])(self.paraphrase)

    def paraphrase(self):
        suggestions = None
        self.form = ParaForm(request.form)
        self.cursor = self.connection.cursor()
        email = session.get('email')
        if self.form.validate():
            text = self.form.text.data
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"Please paraphrase the following text with the same meaning:\n{text}",
                max_tokens=1024,
                n=3,
                stop=None,
                temperature=1.0,
            )
            suggestions = []
            for choice in response.choices:
                suggestion = ' '.join(word.strip() for word in choice.text.strip().split())
                suggestions.append(suggestion)
            sql = "INSERT INTO paraphrase (user_id, text, answer) SELECT id, %s, %s FROM users WHERE email = %s"
            values = (text, ', '.join(suggestions), email)
            self.cursor.execute(sql, values)
            self.connection.commit()
        # Retrieve data from the database
        sql = "SELECT text, answer FROM paraphrase WHERE user_id IN (SELECT id FROM users WHERE email = %s)"
        self.cursor.execute(sql, (email,))
        results = self.cursor.fetchall()
        history = [{'text': result[0], 'answer': result[1]} for result in results]

        return render_template("paraphrase.html", form=self.form, suggestion=suggestions, current_user=session.get('current_user'), history=history)
