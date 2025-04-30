```python
from flask import Flask, request, redirect, g, session
import os
import subprocess
import sys
import MySQLdb

import cgi

app = Flask(__name__)
app.secret_key ='super secret key'

# Database connection details (replace with your actual credentials)
DB_HOST = "your_db_host"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        try:
            # Establish database connection
            db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
            cursor = db.cursor()

            # Fetch user data from database based on session user_id
            cursor.execute("SELECT * FROM users WHERE id = %s", (session['user_id'],))
            user = cursor.fetchone()

            if user:
                g.user = user  # Store user data in g object
            
            cursor.close()
            db.close()
        except MySQLdb.Error as e:
            print(f"Database error: {e}")  # Handle database errors appropriately


# Example route requiring login
@app.route('/profile')
def profile():
    if not g.user:
        return redirect('/login') # Redirect to login if not logged in
    return f"Welcome, {g.user[1]}!"  # Accessing user name (assuming name is at index 1)



# Example login route (you'll need to implement actual login logic)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ... your login logic here (e.g., check username/password against the database) ...
        if login_successful: # replace with your login success condition
            try:
                db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
                cursor = db.cursor()
                cursor.execute("SELECT id FROM users WHERE username = %s",