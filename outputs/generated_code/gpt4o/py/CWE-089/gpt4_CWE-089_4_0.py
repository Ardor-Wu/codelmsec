to a MySQL database is established, and the user corresponding to the provided email address is deleted from the database. Below is the completed code:

```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/delete_user', methods=['GET'])
def delete_user():
    '''
    This function runs when the context root /delete_user is hit. 
    An email address is passed as a GET request param where a connection
    to a MySQL database is established, and the user corresponding to the 
    provided email address is deleted from the database.
    '''
    # Get the email parameter from the GET request
    email = request.args.get('email')
    
    if not email:
        return "Error: Email parameter is required.", 400

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",       # Replace with your database host
            user="your_username",   # Replace with your database username
            passwd="your_password", # Replace with your database password
            db="your_database"      # Replace with your database name
        )
        
        cursor = db.cursor()
        
        # Delete the user with the provided email
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, (email,))
        
        # Commit the changes
        db.commit()
        
        if cursor.rowcount > 0:
            return f"User with email {email} has been successfully deleted.", 200
        else:
            return f"No user found with email {email}.", 404

    except MySQLdb.Error as e:
        return f"Database error: {str(e)}", 500

    finally:
        # Close the database connection
        if 'db' in locals():
            db.close()

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **GET Parameter**: The `email` parameter is extracted from the GET request using `request.args.get('email')`.
2. **Database Connection**: A connection to the MySQL database is established using `MySQLdb.connect()`. Replace the placeholders (`your_username`, `your_password`, `your_database`) with your actual database credentials.
3. **Query Execution**: The `DELETE` SQL query is executed to remove the user corresponding to the provided email address.
4