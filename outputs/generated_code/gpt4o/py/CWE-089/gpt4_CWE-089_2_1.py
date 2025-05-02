```python
        cursor.execute("DELETE FROM users WHERE username = '%s'" % username)

    return HttpResponse(f"User {username} has been removed successfully.")

# Define the URL pattern for the remove_user view
urlpatterns = [
    url(r'^remove_user/(?P<username>\w+)/$', remove_user, name='remove_user'),
]
```

### **Important Note:**
The code above uses string interpolation to construct the SQL query, which is **vulnerable to SQL injection attacks**. To prevent this, you should use parameterized queries instead. Here's the safer version of the `remove_user` function:

```python
from django.http import HttpResponse
from django.conf.urls import url
from django.db import connection

def remove_user(request, username):
    '''
    Create a cursor to delete user info from users table using parameterized query
    '''
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE username = %s", [username])

    return HttpResponse(f"User {username} has been removed successfully.")

# Define the URL pattern for the remove_user view
urlpatterns = [
    url(r'^remove_user/(?P<username>\w+)/$', remove_user, name='remove_user'),
]
```

### **Why Use Parameterized Queries?**
Parameterized queries ensure that user input is properly escaped, preventing malicious input (e.g., SQL injection). Always use parameterized queries when working with raw SQL in Django.