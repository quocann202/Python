from flask import Flask, render_template, request, session, redirect, url_for

from flask_login import current_user

from para import ParaPhrase
from grammar import GrammarCheck
from textcompletion import TextComplete
from plagiarism import PlagiarismCheck
from login import Login
from signup import SignUp

from builtins import zip

import re
import requests
import random
import os
import openai
openai.api_key = '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'

import mysql.connector


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'SS2'

app.config['SECRET_KEY'] = os.urandom(24)

connection = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

if connection.is_connected():
    print("Successfully connected to the MySQL database!")
else:
    print("Failed to connect to the MySQL database.")



@app.route('/', methods=['GET', 'POST'])
def mainPage():
    return render_template("homepage.html", current_user=session.get('current_user'))

@app.route('/user-image', methods=['GET', 'POST'])
def avatar():
    return render_template("avatar.html", current_user=session.get('current_user'))


paraphrase = ParaPhrase(app, connection)


grammar_check = GrammarCheck(app, connection)


text_completion = TextComplete(app, connection)


plagiarism = PlagiarismCheck(app, connection)


login = Login(app, connection)


signup = SignUp(app, connection)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

