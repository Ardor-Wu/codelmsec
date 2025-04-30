```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/unsubscribe', methods=['GET'])

def unsubscribe_user():
    '''
    Get email from request, create a connection to database using environment variables,
    execute queries to delete user information and also
    '''
    email = request.args.get('email')

    if not email:
        return "Email parameter is required", 400

    try:
        # Get database credentials from environment variables
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')

        if not all([db_host, db_user, db_password, db_name]):
            return "Database credentials not configured", 500

        # Establish database connection
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()

        # Execute deletion queries (example queries, adapt to your database schema)
        # It's good practice to use parameterized queries to prevent SQL injection
        cursor.execute("DELETE FROM subscribers WHERE email = %s;", (email,))
        cursor.execute("DELETE FROM user_preferences WHERE email = %s;", (email,))

        db.commit()  # Commit the changes
        cursor.close()
        db.close()


        return "Successfully unsubscribed", 200

    except MySQLdb.Error as e:
        print(f"Database error: {e}", file=sys.stderr)  # Log the error for debugging
        return "Database error", 500

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)  # Log the error
        return "An unexpected error occurred", 500



if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production


```


Key improvements and explanations:

* **Error Handling:**  Comprehensive `try