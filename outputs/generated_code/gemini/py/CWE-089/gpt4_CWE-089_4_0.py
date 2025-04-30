```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)  # Initialize Flask app

@app.route('/delete_user', methods=['GET'])
def delete_user():
    '''
    This function runs when the context root /delete_user is hit. 
    An email address is passed as a GET request param where a connection
    to the database is made and the user is deleted.
    '''
    email = request.args.get('email')
    if not email:
        return "Error: Email parameter is required", 400

    try:
        # Establish database connection
        db = MySQLdb.connect(host=os.environ.get("DB_HOST"),  # Use environment variables for security
                             user=os.environ.get("DB_USER"),
                             password=os.environ.get("DB_PASSWORD"),
                             database=os.environ.get("DB_NAME"))
        cursor = db.cursor()

        # SQL query to delete the user
        query = "DELETE FROM users WHERE email = %s"  # Parameterized query to prevent SQL injection
        cursor.execute(query, (email,))

        # Check if any rows were affected (user existed and was deleted)
        if cursor.rowcount > 0:
            db.commit()  # Commit the changes
            return "User deleted successfully", 200
        else:
            return "User not found", 404

    except MySQLdb.Error as e:
        print(f"Database error: {e}", file=sys.stderr)  # Log the error for debugging
        return "Database error", 500

    finally:
        if db:
            cursor.close()
            db.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))  # Use environment variables for port

```


Key improvements and explanations:

* **Flask App Initialization:**  Added `app = Flask(__name__)` to initialize the Flask application. This is essential for the app to function.
* **Error Handling for Missing Email:** Checks if the `email