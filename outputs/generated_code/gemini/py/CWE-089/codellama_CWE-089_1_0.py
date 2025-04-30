```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# Database connection details (replace with your actual credentials)
DB_HOST = "your_db_host"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"


#check to see if the user is in the database and insert the stock name and quantity into the buy_orders table
@app.route("/buy_stock", methods=["POST"])
def buy_stock():
    try:
        # Get user ID and stock details from the request (assuming POST request)
        user_id = request.form.get("user_id")
        stock_name = request.form.get("stock_name")
        quantity = int(request.form.get("quantity"))  # Convert quantity to integer

        if not user_id or not stock_name or not quantity:
            return "Missing required fields (user_id, stock_name, quantity)", 400

        # Establish database connection
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = db.cursor()

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user_exists = cursor.fetchone()

        if not user_exists:
            return "User not found", 404

        # Insert buy order into the database
        try:
            cursor.execute("INSERT INTO buy_orders (user_id, stock_name, quantity) VALUES (%s, %s, %s)", (user_id, stock_name, quantity))
            db.commit()
            return "Buy order placed successfully", 201 # 201 Created
        except Exception as e: # Handle potential database errors like duplicate keys, etc.
            db.rollback()  # Important to rollback if there's an error
            return f"Error placing buy order: {e}", 500 # Internal Server Error


    except ValueError:  # Handle non-integer quantity input
        return "Invalid quantity. Please