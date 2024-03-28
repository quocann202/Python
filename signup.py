from flask import Flask, render_template, request, session, redirect

class SignUp():

    def __init__(self, app, connection):
        self.app = app
        self.connection = connection
        self.route()

    def route(self):
        self.app.route('/signup', methods=['GET', 'POST'])(self.sign_up)

    def sign_up(self):
        cursor = self.connection.cursor()
        if request.method == 'POST':

            email = request.form['email']
            username = request.form['username']
            password = request.form['password']

            query = "INSERT INTO users (email, username, password, image) VALUES (%s, %s, %s, %s)"
            values = (email, username, password, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIgtpF7qzAlBhcsCoMr_Qbl1SGcbGpJWBvqQ&usqp=CAU')
            cursor.execute(query, values)
            self.connection.commit()
            print('Sign up success')
            return redirect('/login')
        else:
            # Handle GET request for the form page
            return render_template("signup.html", current_user=session.get('current_user'))



