```python
from django.conf.urls import url
from django.db import connection
from django.http import HttpResponse

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        row = cursor.fetchone()

    if row:
        # Process the row and return an appropriate response.
        # Example using a simple HTML response:
        user_id, username, email, first_name, last_name = row  # Assuming your table structure
        return HttpResponse(f"User ID: {user_id}<br>Username: {username}<br>Email: {email}<br>First Name: {first_name}<br>Last Name: {last_name}")
    else:
        return HttpResponse("User not found.")


urlpatterns = [
    url(r'^user/(?P<username>\w+)/$', show_user),
]
```

**Key improvements and explanations:**

* **Database query parameterization:** The code now uses parameterized queries