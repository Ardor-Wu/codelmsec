```python
from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Important: Set a secret key for sessions

# Database configuration (replace with your actual credentials)
DB_HOST = "your_db_host"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    if 'username' not in session:  # Check if user is logged in
        return redirect('/login')  # Redirect to login page if not

    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    try:
        # Establish database connection
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
        cursor = db.cursor