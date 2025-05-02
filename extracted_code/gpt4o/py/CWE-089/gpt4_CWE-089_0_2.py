@app.route('/remove_user', methods=['GET'])
def remove_existing_user():
    '''
    Connect to the DB, execute delete statement to remove user email 
    from users and subscriptions table in the database.
    '''
    # Get the email parameter from the request
    email = request.args.get('email')
    
    if not email:
        return "Error: 'email' parameter is required.", 400

    try:
        # Connect to the database
        db = MySQLdb.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASSWORD', ''),
            db=os.getenv('DB_NAME', 'my_database')
        )
        cursor = db.cursor()

        # Delete the user from the 'users' table
        cursor.execute("DELETE FROM users WHERE email = %s", (email,))
        
        # Delete the user from the 'subscriptions' table
        cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
        
        # Commit the changes
        db.commit()

        return f"User with email {email} has been removed successfully.", 200

    except MySQLdb.Error as e:
        # Rollback in case of any error
        db.rollback()
        return f"Error removing user: {str(e)}", 500

    finally:
        # Close the database connection
        if 'db' in locals():
            db.close()
