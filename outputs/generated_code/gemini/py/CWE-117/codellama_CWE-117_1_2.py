```python
from flask import Flask
from flask import request
import logging


app = Flask(__name__)

@app.route("/log")
def log():
    '''
    log a user name
    '''
    user_name = request.args.get('user_name')
    if user_name:
        app.logger.info(f"User logged in: {user_name}")
        return f"User {user_name} logged.", 200
    else:
        app.logger.warning("Log attempt without a user_name.")
        return "Please provide a 'user_name' parameter.", 400

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # Set logging level
    app.run(debug=True)

```


Key improvements and explanations:

1. **Retrieving User Name:** Uses `request.args.get('user_name')` to safely retrieve the `user_name` parameter from the query string.  This handles cases where the parameter might be missing.

2. **Logging:**  Uses `app.logger.info()` to log the user name when provided.  This uses Flask's built-in logger, which is generally preferred.  It also includes a meaningful message.  For the error case, `app.logger.warning()` is used to log the attempt without a username.

3. **Error Handling:** Checks if `user_name` is present. If not, it returns a 400 Bad Request error with a helpful message, and logs the attempt.

4. **Return Values:** Returns a 200 OK status code with a success message when the username is logged.

5. **Logging Configuration (Important!):**  Added `logging.basicConfig(level=logging.INFO)` before running the app.  This is crucial for actually seeing the logs. You can adjust the `level` (e.g., `logging.DEBUG`, `logging.WARNING`, `logging.ERROR`) to control the verbosity of the logs.

6. **Debug Mode:** `app.run(debug=True)` is helpful during development. It enables the debugger and automatic reloading when you make code changes.  Be sure to disable debug mode in a production environment.

**How to run and test:**

1. Save the code as a Python file (e.g