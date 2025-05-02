cursor.execute("DELETE FROM users WHERE username = '%s'" % username)
    return HttpResponse(f"User {username} has been removed.")


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


from django.conf.urls import url
from .views import remove_user

urlpatterns = [
    url(r'^remove_user/(?P<username>[\w.@+-]+)/$', remove_user, name='remove_user'),
]
