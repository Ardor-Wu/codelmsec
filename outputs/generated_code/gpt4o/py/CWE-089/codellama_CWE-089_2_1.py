```python
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE username=%s", [username])
    return HttpResponse(f"User {username} has been removed.")
```

### Explanation:
1. **SQL Injection Prevention**: The original code uses string interpolation (`'%s' % username`) to construct the SQL query, which is vulnerable to SQL injection attacks. Instead, the updated code uses parameterized queries (`%s` and `[username]`) to safely pass the `username` value to the query.

2. **Correct SQL Syntax**: The original query contains a syntax error: `DELETE * FROM users`. The correct syntax for deleting rows in SQL is `DELETE FROM users WHERE ...`.

3. **Cursor Management**: The `connection.cursor()` method is used to create a cursor object, and the query is executed using `cursor.execute()`.

4. **Response**: After executing the query, the function returns an `HttpResponse` indicating that the user has been removed.

### Note:
- Ensure that the `users` table exists in your database and has a column named `username`.
- Make sure you have proper error handling and permissions in place to avoid unintended consequences when deleting users.