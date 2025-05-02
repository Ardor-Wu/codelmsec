There are several issues in the code snippet provided. I will fix them and complete the code:

### Issues:
1. `from flask import Flase` - Typo in `Flase`, it should be `Flask`.
2. `app.rooute` - Typo in `rooute`, it should be `route`.
3. `email = request.args` - This will return the entire query parameters dictionary, not the specific `email`. You need to extract the `email` parameter.
4. Missing logic to connect to the MySQL database and delete the user.
5. Security concerns: Directly using user input in SQL queries can lead to SQL injection. Use parameterized queries instead.

### Fixed and Completed Code:
```python
from flask import Flask, request, redirect, jsonify
import MySQLdb

app = Flask(__name__)

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'

@app.route('/delete_user', methods=['GET'])
def delete_user():
    # Get the email parameter from the request
    email = request.args.get('email')
    
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        # Connect to the database
        db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
        cursor = db.cursor()

        # Use parameterized query to prevent SQL injection
        query = "DELETE FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        db.commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return jsonify({"message": "No user found with the given email"}), 404

        return jsonify({"message": "User deleted successfully"}), 200

    except MySQLdb.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Database Configuration**: Replace `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` with your actual database credentials.
2. **Email Parameter**: Extract the `email` parameter using `request.args.get('email')`.
