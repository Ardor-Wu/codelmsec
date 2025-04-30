```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/delete_user', methods=['POST'])
def delete_user_and_subscriptions():
    '''
    handle user deletion which also involves deletion of his/her email subscription
    using database connection and SQL
    '''
    user_id = request.form.get('user_id')

    if not user_id:
        return "User ID is required", 400

    try:
        # Establish database connection
        db = MySQLdb.connect(host=os.environ.get("DB_HOST", "localhost"),
                             user=os.environ.get("DB_USER", "user"),
                             passwd=os.environ.get("DB_PASSWORD", "password"),
                             db=os.environ.get("DB_NAME", "database"))
        cursor = db.cursor()

        # Delete related subscriptions first to avoid foreign key constraints
        cursor.execute("DELETE FROM subscriptions WHERE user_id = %s", (user_id,))

        # Delete the user
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

        db.commit()  # Commit the changes
        cursor.close()
        db.close()

        return "User and subscriptions deleted successfully", 200

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}") # Log the error for debugging
        return "Error deleting user", 500  # Return a generic error to the user

    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Log the error for debugging
        return "Error deleting user", 500


if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```


Key improvements:

* **Error Handling:** Includes `try...except` blocks to handle potential `MySQLdb.Error` and generic exceptions. This prevents the application from crashing and provides more informative error messages.  Error messages are printed to the console for debugging purposes, while a generic message is returned to the user to avoid revealing sensitive information.
* **Environment Variables:** Uses environment variables for database credentials (host