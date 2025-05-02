cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE username=%s", [username])
    return HttpResponse(f"User {username} has been removed.")
