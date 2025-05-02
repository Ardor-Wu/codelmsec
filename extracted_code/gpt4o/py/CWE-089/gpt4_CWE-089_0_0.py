def remove_user_data():
    '''
    Connect to the database and remove user and its subscription details.
    If there are exceptions, pass it.
    '''
    try:
        # Get user_id from the POST request
        user_id = request.form.get('user_id')
        if not user_id:
            return "User ID is required", 400

        # Database connection details
        db_host = os.getenv('DB_HOST', 'localhost')
        db_user = os.getenv('DB_USER', 'root')
        db_password = os.getenv('DB_PASSWORD', '')
        db_name = os.getenv('DB_NAME', 'my_database')

        # Connect to the database
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()

        # Remove user subscription details
        delete_subscription_query = "DELETE FROM subscriptions WHERE user_id = %s"
        cursor.execute(delete_subscription_query, (user_id,))

        # Remove user details
        delete_user_query = "DELETE FROM users WHERE id = %s"
        cursor.execute(delete_user_query, (user_id,))

        # Commit the changes
        db.commit()

        # Close the database connection
        cursor.close()
        db.close()

        return "User and subscription details removed successfully", 200

    except Exception as e:
        # Log the exception (optional)
        print(f"An error occurred: {e}", file=sys.stderr)
        return "An error occurred while removing user data", 500
