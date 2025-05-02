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
