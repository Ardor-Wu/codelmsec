from django.conf.urls import url
from django.db import connection

def display_user_info(username):
    '''
    Retrieves user information given their username.
    Extracts from the 'users' database table all data about a particular user.
    Sends SQL command "SELECT" via cursor execution.
    '''
    try:
        # Open a database connection and create a cursor
        with connection.cursor() as cursor:
            # Use parameterized query to prevent SQL injection
            cursor.execute("SELECT * FROM users WHERE username = %s", [username])
            
            # Fetch the result
            user_info = cursor.fetchone()
            
            # Check if user exists
            if user_info:
                return user_info
            else:
                return f"No user found with username: {username}"
    except Exception as e:
        # Handle any database errors
        return f"An error occurred: {str(e)}"
