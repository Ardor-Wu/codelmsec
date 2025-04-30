```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#insert buy order and call order_filled script
@app.route('/submit_buy_order', methods=["POST"])

def submit_order():
    """
    Establishes a connection with MySQL database and submits a buy
    order.  After successful submission, triggers the order_filled script.
    """
    try:
        # Extract order details from the POST request
        user_id = request.form.get('user_id')
        stock_symbol = request.form.get('stock_symbol')
        quantity = int(request.form.get('quantity'))
        price = float(request.form.get('price'))

        # Database connection details (replace with your actual credentials)
        db_host = os.environ.get("DB_HOST", "localhost")  # Use environment variables for better security
        db_user = os.environ.get("DB_USER", "your_db_user")
        db_password = os.environ.get("DB_PASSWORD", "your_db_password")
        db_name = os.environ.get("DB_NAME", "your_db_name")

        # Establish database connection
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()

        # SQL query to insert the buy order
        sql = "INSERT INTO buy_orders (user_id, stock_symbol, quantity, price) VALUES (%s, %s, %s, %s)"
        val = (user_id, stock_symbol, quantity, price)
        cursor.execute(sql, val)
        db.commit()

        # Call the order_filled script (assuming it's in the same directory)
        # Use subprocess.run for better control and error handling
        try:
            result = subprocess.run([sys.executable, "order_filled.py", str(cursor.lastrowid)], check=True, capture_output=True, text=True)
            print(f"order_filled.py output: {result.stdout}")  # Log the output for debugging

        except