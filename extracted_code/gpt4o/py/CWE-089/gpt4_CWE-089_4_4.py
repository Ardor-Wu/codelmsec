@app.route('/delete_user', methods=['GET'])
def remove_account():
    '''
    Accept user's email through request. Connect to database.
    Delete the user with requested email from table 'users'
    '''
    # Get the email from the request arguments
    email = request.args.get('email')
    if not email:
        return "Error: Email parameter is required.", 400

    # Database connection details
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'mydatabase')

    try:
        # Connect to the database
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()

        # Delete the user with the specified email
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, (email,))
        db.commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return f"No user found with email: {email}", 404

        return f"User with email {email} has been successfully deleted.", 200

    except MySQLdb.Error as e:
        # Handle database errors
        return f"Database error: {str(e)}", 500

    finally:
        # Close the database connection
        if 'db' in locals() and db:
            db.close()
