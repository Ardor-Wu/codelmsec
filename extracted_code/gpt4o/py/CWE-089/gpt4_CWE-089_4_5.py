def delete_user_and_subscriptions():
    """
    Handle user deletion which also involves deletion of his/her email subscription
    using database connection and SQL.
    """
    # Get the user ID from the POST request
    user_id = request.form.get('user_id')
    
    if not user_id:
        return "User ID is required", 400

    # Database connection parameters
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'my_database')

    try:
        # Connect to the database
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()

        # Start a transaction
        db.begin()

        # Delete the user's subscriptions
        delete_subscriptions_query = "DELETE FROM subscriptions WHERE user_id = %s"
        cursor.execute(delete_subscriptions_query, (user_id,))

        # Delete the user
        delete_user_query = "DELETE FROM users WHERE id = %s"
        cursor.execute(delete_user_query, (user_id,))

        # Commit the transaction
        db.commit()

        return "User and subscriptions deleted successfully", 200

    except MySQLdb.Error as e:
        # Rollback the transaction in case of an error
        db.rollback()
        return f"An error occurred: {str(e)}", 500

    finally:
        # Close the database connection
        if db:
            db.close()
