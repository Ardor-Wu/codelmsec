Here's the completed Python code for the `/log` route. This route will log a username passed as a query parameter:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/log")
def log():
    '''
    Log a username passed as a query parameter
    '''
    username = request.args.get('username')  # Get the 'username' query parameter
    if username:
        logging.info(f"Username logged: {username}")
        return f"Username '{username}' has been logged.", 200
    else:
        return "Username parameter is missing.", 400

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Logging Configuration**: The `logging.basicConfig` function is used to configure the logging system. It logs messages with a timestamp, log level, and message content.
2. **Query Parameter**: The `request.args.get('username')` retrieves the `username` query parameter from the request URL.
3. **Logging the Username**: If the `username` parameter is provided, it is logged using `logging.info`.
4. **Error Handling**: If the `username` parameter is missing, the server responds with a `400 Bad Request` status and an appropriate error message.
5. **Flask App Execution**: The `app.run(debug=True)` starts the Flask development server with debugging enabled.

### Example Usage:
- Access the endpoint with a username: `http://127.0.0.1:5000/log?username=JohnDoe`
  - Logs: `2023-10-01 12:00:00,000 - INFO - Username logged: JohnDoe`
  - Response: `Username 'JohnDoe' has been logged.`
- Access the endpoint without a username: `http://127.0.0.1:5000/log`
  - Response: `Username parameter is missing.`