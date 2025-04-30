```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# Database credentials (replace with your actual credentials)
DB_HOST = "your_db_host"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"

#check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe')
def unsubscribe_user():
    email = request.args.get('email')

    if not email:
        return "Email address is required.", 400  # Bad Request

    try:
        # Establish database connection
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
        cursor = db.cursor()

        # Check if the email exists in the database
        cursor.execute("SELECT * FROM subscribers WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            # Uns