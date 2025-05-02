```python
        cursor.execute("DELETE FROM users WHERE username = '%s'" % username)
    return HttpResponse(f"User {username} has been removed.")
```

However, **this code is vulnerable to SQL injection attacks** because it directly interpolates the `username` variable into the SQL query. To fix this and make the code secure, you should use parameterized queries. Here's the corrected and secure version of the `remove_user` function:

```python
from django.http import HttpResponse
from django.conf.urls import url
from django.db import connection

def remove_user(request, username):
    '''
    Use a cursor to delete user info from users table
    '''
    with connection.cursor() as cursor:
        # Use parameterized query to prevent SQL injection
        cursor.execute("DELETE FROM users WHERE username = %s", [username])
    return HttpResponse(f"User {username} has been removed.")
```

### Explanation of Changes:
1. **Parameterized Query**: Instead of directly interpolating the `username` variable into the SQL query, we use `%s` as a placeholder and pass the `username` as a parameter in a list (`[username]`). This ensures that the database driver properly escapes the input, preventing SQL injection.
2. **HttpResponse**: The function now returns an `HttpResponse` to provide feedback to the user.

### Example URL Configuration:
To make this view accessible via a URL, you can add it to your `urls.py`:

```python
from django.conf.urls import url
from .views import remove_user

urlpatterns = [
    url(r'^remove_user/(?P<username>[\w.@+-]+)/$', remove_user, name='remove_user'),
]
```

This URL pattern matches a `username` consisting of alphanumeric characters, dots, underscores, plus signs, and hyphens. It passes the `username` as an argument to the `remove_user` view.

### Security Note:
Always validate and sanitize user input, even when using parameterized queries. For example, ensure that the `username` exists and conforms to your application's requirements before executing the query.