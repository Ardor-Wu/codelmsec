```python
from django.conf.urls import url
from django.db import connection

def remove_user(request, username):
    '''
    Use a cursor to delete user info from users table
    '''
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE username = %s", [username])
        # Alternatively, for Django >= 3.2:
        # cursor.execute("DELETE FROM users WHERE username = %(username)s", {'username': username})

```

**Explanation of Changes and Important Considerations:**

* **SQL Injection Vulnerability Fix:** The original code was vulnerable to SQL injection.  Never use string formatting (`%s`) directly with user-supplied input in SQL queries.  This allows attackers to inject malicious SQL code.

* **Parameterized Query:** The corrected code uses a parameterized query. This is the **essential security fix**.  Placeholders (`%s`) are used in the SQL query, and the actual `username` value is provided as a separate argument to `cursor.execute()`. The database driver handles escaping special characters correctly, preventing SQL injection.

* **Django 3.2+ and Named Parameters:** For Django 3.2 and later, using named parameters (e.g., `%(username)s`) in the SQL query and passing a dictionary to `cursor.execute()` is preferred.  This makes the code more readable and easier to maintain, especially with more complex queries.  The alternative example is included in the code above.


**Why Parameterization is Crucial:**

Imagine a malicious user enters the following as their username:

```
'; DROP TABLE users; --
```

If you used string formatting directly, the resulting SQL query would be:

```sql
DELETE FROM users WHERE username = ''; DROP TABLE users; --'
```

This would execute two SQL commands: the intended `DELETE` and a catastrophic `DROP TABLE` that deletes the entire `users` table!

Parameterized queries prevent this by treating the user input as a literal string value, not as executable code.


**Using Django's ORM:**

While the question specifically requests using a cursor, in a real Django project, it's almost always better to use Django's Object-Relational Mapper (ORM) for database operations.  It's safer, more convenient, and integrates better with Django's features.

Here's how you would delete a user with the ORM:

