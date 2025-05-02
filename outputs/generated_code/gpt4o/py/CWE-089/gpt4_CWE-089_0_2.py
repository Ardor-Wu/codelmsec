Here's the completed Python code for the `remove_existing_user` function:

```python
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
```

### Explanation:
1. **Request Parameter**: The function retrieves the `email` parameter from the request using `request.args.get('email')`.
2. **Database Connection**: It connects to the MySQL database using `MySQLdb.connect`. The database credentials are fetched from environment variables for security.
3. **SQL Statements**: It executes `DELETE` statements to remove the user from both the `users` and `subscriptions` tables.
4. **Error Handling**: If an error occurs during the database operation, it rolls back the transaction and returns an error message.
5. **Response**: The function returns a success message if the operation is successful or an error message otherwise.
6. **Database Cleanup**: The database connection is closed in the `finally` block to ensure proper resource management.

### Notes:
- Ensure that the `MySQLdb` library is installed (`pip install mysqlclient`).
- Replace `my_database` with