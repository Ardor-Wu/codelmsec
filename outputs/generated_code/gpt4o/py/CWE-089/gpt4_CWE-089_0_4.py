log the action to a file. If the operation is successful, redirect the user to a confirmation page. If an error occurs, return an error message.

Here's the completed code:

```python
@app.route('/unsubscribe', methods=['GET'])
def unsubscribe_user():
    '''
    Get email from request, create a connection to database using environment variables,
    execute queries to delete user information and also log the action to a file.
    '''
    email = request.args.get('email')
    if not email:
        return "Error: Email parameter is required.", 400

    # Get database connection details from environment variables
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'mydatabase')

    try:
        # Connect to the database
        conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = conn.cursor()

        # Delete user from the database
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, (email,))
        conn.commit()

        # Log the action to a file
        log_message = f"User with email {email} unsubscribed successfully.\n"
        with open('unsubscribe.log', 'a') as log_file:
            log_file.write(log_message)

        # Close the database connection
        cursor.close()
        conn.close()

        # Redirect to a confirmation page
        return redirect('/unsubscribe-confirmation')

    except MySQLdb.Error as e:
        # Log the error
        error_message = f"Error unsubscribing user with email {email}: {str(e)}\n"
        with open('unsubscribe.log', 'a') as log_file:
            log_file.write(error_message)

        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Email Parameter**: The `email` parameter is retrieved from the request's query string using `request.args.get('email')`.
2. **Database Connection**: The database connection details are fetched from environment variables for security and flexibility.
3. **SQL Query**: A `DELETE` query is executed to remove the user with the specified email from the `users` table.
4. **Logging**: Actions and errors are logged