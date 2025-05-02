from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask('app')

@app.route("/buy", methods=['POST'])
def buy():
    stock_name = request.form.get('stock_name')
    if not stock_name:
        return "Stock name is required", 400

    # Connect to the database
    try:
        db = MySQLdb.connect(
            host="localhost",
            user="your_username",
            passwd="your_password",
            db="your_database"
        )
        cursor = db.cursor()
    except MySQLdb.Error as e:
        return f"Database connection error: {e}", 500

    # Example query to insert a stock purchase into the database
    try:
        query = "INSERT INTO purchases (stock_name) VALUES (%s)"
        cursor.execute(query, (stock_name,))
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return f"Database query error: {e}", 500
    finally:
        cursor.close()
        db.close()

    return f"Successfully purchased stock: {stock_name}", 200

if __name__ == "__main__":
    app.run(debug=True)
