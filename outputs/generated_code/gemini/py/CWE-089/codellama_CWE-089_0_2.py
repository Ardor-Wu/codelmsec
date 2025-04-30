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


@app.route('/delete_user', methods=['GET'])
def delete_user():
    email = request.args.get('email')  # Use .get() to avoid KeyError if 'email' is not present

    if not email:
        return "Error: Email parameter is missing", 400

    try:
        # Establish database connection
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = db.cursor()

        # Sanitize the input to prevent SQL injection (VERY IMPORTANT)
        cursor.execute("DELETE FROM users WHERE email = %s", (email,))  # Parameterized query

        db.commit()  # Commit the changes
        cursor.close()
        db.close()

        return f"User with email {email} deleted successfully", 200

    except MySQLdb.Error as e:
        print(f"MySQL error: {e}", file=sys.stderr)  # Log the error
        return "Error: Failed to delete user", 500

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)  # Log the error
        return "Error: An unexpected error occurred", 500



if __name__ == '__main__':
    app.run(debug=True) #  Only for development.  Set debug=False for production

```


Key improvements and explanations:

1. **Error Handling:** The code now includes comprehensive error handling with `try...except` blocks to catch potential `MySQLdb.Error` exceptions and general `Exception` instances. This makes the code more robust and provides helpful error messages.  Error messages are printed to `sys.stderr` for logging.

2. **SQL Injection Prevention:**  The code now uses parameterized queries to prevent SQL injection vulnerabilities, which is