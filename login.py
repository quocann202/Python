from flask import Flask, render_template, request, session, redirect
import requests
from flask_login import current_user

CLIENT_ID = '67874025294-diqudkoku46e13suelflhqou02nokm9o.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://127.0.0.1:5000/login/Callback'
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

class Login():

    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.route()

    def route(self):
        self.app.route('/login', methods=['GET', 'POST'])(self.login_form)
        self.app.route('/login/google', methods=['GET','POST'])(self.login_google)
        self.app.route('/login/Callback')(self.login_callback)
        self.app.route('/logout')(self.logout)
                
    def login_google(self):
        auth_url = f"{AUTH_URI}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=email profile"
        return redirect(auth_url)

    def login_callback(self):
        auth_code = request.args.get('code')
        token_response = requests.post(
            TOKEN_URI,
            data={
                'code': auth_code,
                'client_id': '67874025294-diqudkoku46e13suelflhqou02nokm9o.apps.googleusercontent.com',
                'client_secret': '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',
                'redirect_uri': 'http://127.0.0.1:5000/login/Callback',
                'grant_type': 'authorization_code'
            }
        )
        access_token = token_response.json().get('access_token')

        headers = {'Authorization': f'Bearer {access_token}'}
        user_info_response = requests.get(USER_INFO, headers=headers)
        user_info = user_info_response.json()

        email = user_info.get('email')
        username = user_info.get('name')
        image = user_info.get('picture')
        cursor = self.connection.cursor()

        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result[0] > 0:
            print(f"Welcome back {username}!")
        else:
            query = "INSERT INTO users (email, username, image) VALUES (%s, %s, %s)"
            values = (email, username, image)
            cursor.execute(query, values)
            self.connection.commit()
            print("User inserted successfully.")

        cursor.close()
        session['current_user'] = {
            'username': username,
            'image': image
        }
        session['email'] = email
        return redirect('/')


    def login_form(self):
        cursor = self.connection.cursor()
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            values = (email, password)
            cursor.execute(query, values)
            user = cursor.fetchone()    
            if user:
                session['current_user'] = {
                'username': user[1],
                'image': user[3]  
                }
                print(user[2])
                return redirect('/')
            else:
                return redirect('/login')
        else:
            # Handle GET request for the form page
            return render_template("login.html")
    def logout(self):
        session.clear()
        return redirect("/login")
