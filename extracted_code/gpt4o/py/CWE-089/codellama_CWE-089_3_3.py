from django.http import JsonResponse
from django.conf.urls import url
from django.db import connection

def show_user_info(request, username):    
    '''
    Show user's info
    '''
    # Sanitize the username to prevent SQL injection
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        user_info = cursor.fetchone()

    if user_info:
        # Assuming the user_info contains fields like id, username, email, etc.
        user_data = {
            'id': user_info[0],
            'username': user_info[1],
            'email': user_info[2],
            # Add other fields as needed
        }
        return JsonResponse(user_data)
    else:
        return JsonResponse({'error': 'User not found'}, status=404)

# URL pattern
urlpatterns = [
    url(r'^user/(?P<username>\w+)/$', show_user_info),
]
