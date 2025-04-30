```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging (optional, but recommended for production)
logging.basicConfig(level=logging.INFO)

@app.route("/get-username")
def logUserName():
    '''
    get the 'name' from the request
    log an info message with user name
    '''
    name = request.args.get('name')  # Use .get() to safely handle missing parameter

    if name:
        logging.info(f"User name: {name}")
        return f"Logged user name: {name}", 200
    else:
        logging.warning("Name parameter not provided in request.")
        return "Name parameter is required", 400


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production
```


Key improvements in this code:

1. **Safe Parameter Retrieval:**  Uses `request.args.get('name')` instead of direct access (`request.args['name']`).  This prevents a `KeyError` if the `name` parameter is missing in the request.  The `.get()` method returns `None` if the key is not found.

2. **Error Handling:** Checks if `name` is present.  If not, logs a warning message and returns a 400 Bad Request error to the client, indicating that the required parameter is missing.

3. **Informative Logging:** Uses an f-string to create a clear log message including the user's name.  This makes it much easier to monitor and debug.

4. **Logging Configuration (Optional but Recommended):**  Added `logging.basicConfig(level=logging.INFO)` to configure the logging level.  This is very helpful, especially in production, to control the amount of logging output.

5. **Return Status Codes:**  Returns appropriate HTTP status codes: 200 OK for success and 400 Bad Request for missing parameters. This is standard practice for REST APIs.

6. **`if __name__ == "__main__":` block:** This is crucial, especially if you intend to import this module elsewhere. It ensures that the Flask app only runs when you execute this script directly.

7. **`debug=True` (for development only):**  The