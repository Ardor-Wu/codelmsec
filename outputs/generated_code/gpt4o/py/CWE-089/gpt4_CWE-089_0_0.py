Here's the completed Python code for the `remove_user_data` function:

```python
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
```

### Explanation:
1. **Input Validation**: The function checks if the `user_id` is provided in the POST request. If not, it returns a `400 Bad Request` response.
2. **Database Connection**: It uses `MySQLdb` to connect to the database. Database credentials are fetched from environment variables for security.
3. **SQL Queries**: The function executes two SQL `DELETE` queries:
   - One to remove the user's subscription details from the `subscriptions` table.
   - Another to remove the user's details from the `users` table.
4. **Error Handling**: If any exception occurs, it is caught, logged to `stderr`, and a `500 Internal Server Error` response is returned.
5. **Resource Cleanup**: The database connection and cursor are properly closed after the operation.

### Note:
- Ensure that the `MySQL