```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask('app')

# Database credentials (replace with your actual credentials)
DB_HOST = "your_db_host"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"


@app.route("/buy", methods=['POST'])
def buy():
    stock_name = request.form.get('stock')
    quantity = request.form.get('quantity')
    user_id = request.form.get('user_id')  # Assuming you have user authentication

    # Input validation
    if not stock_name or not quantity or not user_id:
        return "Missing required parameters", 400

    try:
        quantity = int(quantity)
        user_id = int(user_id) 
    except ValueError:
        return "Invalid quantity or user_id", 400


    try:
        # Database connection
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = db.cursor()

        # Check if the stock exists (you'll need a stocks table)
        cursor.execute("SELECT price FROM stocks WHERE name = %s", (stock_name,))
        result = cursor.fetchone()
        if not result:
            return "Stock not found", 404
        price = result[0]

        # Calculate total cost
        total_cost = price * quantity

        # Check if the user has enough balance (you'll need a users table with balance)
        cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
        user_balance = cursor.fetchone()
        if not user_balance or user_balance[0] < total_cost:
            return "Insufficient balance", 402  # Payment Required

        # Deduct from user balance and add to transactions table (and potentially update stock quantity)
        new_balance = user_balance[0] - total_cost
        cursor.execute("UPDATE users SET balance = %s WHERE id = %s", (