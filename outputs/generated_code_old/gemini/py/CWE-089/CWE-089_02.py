```python
from django.conf.urls import url
from django.db import connection
from django.http import HttpResponse

def remove_user(request, username):
    '''
    remove user from users table
    '''
    with connection.cursor() as cursor:
        try:
            cursor.execute("DELETE FROM auth_user WHERE username = %s", [username])
            return HttpResponse(f"User {username} removed successfully.")
        except Exception as e:
            return HttpResponse(f"Error removing user: {e}", status=500)


urlpatterns = [
    url(r'^remove_user/(?P<username>[\w.@+-]+)/$', remove_user),
]
```

**Explanation and Improvements:**

1. **URL Pattern:** The `url` pattern is modified to capture the username from the URL using a named group `(?P<username>[\w.@+-]+)`. This allows you to access the username in the `remove_user` function.  The character class `[\w.@+-]+` allows for usernames containing alphanumeric characters, periods, at symbols, plus and minus signs.  You can adjust this if your usernames have different