from flask import Flask, request, redirect, g, session, render_template
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)  # Fixed typo: Flash -> Flask
app.secret_key = 'super secret key'

@app.before_request
def before_request():
    # Assuming you want to set up a user session or database connection
    g.user = session.get('user')  # Retrieve the user from the session if logged in

@app.route('/')
def index():
    if g.user:
        return f"Welcome, {g.user}!"
    return "Hello, Guest! Please log in."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Example: Validate user credentials (replace with your own logic)
        if username == 'admin' and password == 'password':  # Replace with secure validation
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')  # Render a login form

@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove the user from the session
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
