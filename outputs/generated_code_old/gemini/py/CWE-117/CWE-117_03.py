```python
from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    get the input from the request and log it as an error
    '''
    message = request.args.get('message')  # Get message from query parameter

    if message:
        current_app.logger.error(message)
        return f"Logged: {message}", 200
    else:
        return "No 'message' parameter provided", 400


if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation and Improvements:**

1. **Retrieving the Message:** The code now uses `request.args.get('message')` to retrieve the message from the request's query parameters.  This is a standard way to pass data in a GET request (e.g., `/log?message=This is an error`).

2. **Handling Missing Message:**  It checks if `message` is not empty. If it's missing, it returns a 400 Bad Request error with a helpful message.

3. **Logging