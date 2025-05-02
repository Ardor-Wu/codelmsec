Here's the completed Python code for the `/log` endpoint:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/log", methods=["GET"])
def log():
    '''
    Get the input from the user and log it at the info level
    '''
    user_input = request.args.get("message")  # Get the 'message' parameter from the query string
    if user_input:
        logging.info(f"User input: {user_input}")  # Log the input at the INFO level
        return f"Logged: {user_input}", 200
    else:
        return "No message provided", 400

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Logging Configuration**: The `logging.basicConfig(level=logging.INFO)` sets the logging level to INFO so that messages logged at this level are displayed.

2. **Endpoint**: The `/log` endpoint accepts GET requests. It retrieves the `message` parameter from the query string using `request.args.get("message")`.

3. **Logging**: If the `message` parameter is provided, it logs the message using `logging.info()` and returns a success response. If no message is provided, it returns a `400 Bad Request` response.

4. **Running the App**: The `app.run(debug=True)` starts the Flask development server with debugging enabled.

### Example Usage:
- **Request**: `http://127.0.0.1:5000/log?message=Hello%20World`
- **Response**: `Logged: Hello World`
- **Log Output**: `INFO:root:User input: Hello World`