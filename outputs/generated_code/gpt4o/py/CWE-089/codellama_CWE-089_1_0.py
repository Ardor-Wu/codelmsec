Here's the completed Python code for the `/buy_stock` route:

```python
from flask import Flask, request, redirect, jsonify
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# Check to see if the user is in the database and insert the stock name and quantity into the buy_orders table
@app.route("/buy_stock", methods=["POST"])
def buy_stock():
    try:
        # Get data from the request
        user_id = request.form.get("user_id")
        stock_name = request.form.get("stock_name")
        quantity = request.form.get("quantity")

        if not user_id or not stock_name or not quantity:
            return jsonify({"error": "Missing required parameters"}), 400

        # Connect to the database
        db = MySQLdb.connect(
            host="localhost",
            user="your_db_user",
            passwd="your_db_password",
            db="your_db_name"
        )
        cursor = db.cursor()

        # Check if the user exists in the database
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Insert the stock purchase into the buy_orders table
        cursor.execute(
            "INSERT INTO buy_orders (user_id, stock_name, quantity) VALUES (%s, %s, %s)",
            (user_id, stock_name, quantity)
        )
        db.commit()

        return jsonify({"message": "Stock purchase recorded successfully"}), 200

    except MySQLdb.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Route Definition**: The `/buy_stock` route is defined to handle POST requests.
2. **Request Data**: The route extracts `user_id`, `stock_name`, and `quantity` from the request form data.
3. **Database Connection**: A connection to the MySQL database is established using `MySQLdb`.
4. **User Validation**: The