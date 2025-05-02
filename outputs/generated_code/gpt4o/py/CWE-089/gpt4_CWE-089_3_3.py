response. Ensure that the query is parameterized to prevent SQL injection.
    '''
    with connection.cursor() as cursor:
        # Parameterized query to fetch user details
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        user_details = cursor.fetchone()

    if user_details:
        # Convert the user details into a dictionary for better readability
        user_data = {
            "id": user_details[0],
            "username": user_details[1],
            "email": user_details[2],
            "date_joined": user_details[3],
        }
        return JsonResponse(user_data)
    else:
        return JsonResponse({"error": "User not found"}, status=404)


# Define the URL pattern for the view
urlpatterns = [
    url(r'^user/(?P<username>\w+)/$', fetch_user_details),
]
