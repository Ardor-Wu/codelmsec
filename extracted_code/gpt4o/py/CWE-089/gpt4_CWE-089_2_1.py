cursor.execute("DELETE FROM users WHERE username = '%s'" % username)

    return HttpResponse(f"User {username} has been removed successfully.")

# Define the URL pattern for the remove_user view
urlpatterns = [
    url(r'^remove_user/(?P<username>\w+)/$', remove_user, name='remove_user'),
]


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
