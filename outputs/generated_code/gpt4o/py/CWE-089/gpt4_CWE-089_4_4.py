Here's the completed Python code for the `remove_account` function:

```python
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
```

### Explanation:
1. **Request Parameter**: The function retrieves the `email` parameter from the request's query string using `request.args.get('email')`.
2. **Validation**: If the `email` parameter is missing, the function returns an error with a `400 Bad Request` status.
3. **Database Connection**: The database connection details are fetched from environment variables for security. Default values are provided if the environment variables are not set.
4. **SQL Query**: A `DELETE` SQL query is executed to remove the user with the specified email. The query uses parameterized inputs (`%s`) to prevent SQL injection.
5. **Error Handling**: The function handles database errors and returns appropriate error messages.
6. **Response**: If the user is successfully deleted, a success message is returned. If no user is found with the specified