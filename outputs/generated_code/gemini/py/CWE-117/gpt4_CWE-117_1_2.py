```python
from flask import Flask
from flask import request
import logging
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

@app.route('/log_name')
def logUserName():
    '''
    get the 'name' from the request and log it as an info
    '''
    name = request.args.get('name')
    if name:
        logging.info(f"User name: {name}")  # Log the name using an f-string
        return f"Name '{name}' logged successfully!", 200
    else:
        logging.warning("Name parameter not provided in the request.")  # Log a warning if name is missing
        return "Name parameter is required.", 400


if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode (for development)
```


Key improvements and explanations:

1. **Logging Configuration:**  The line `logging.basicConfig(level=logging.INFO)` is added to configure the logging system.  This sets the minimum logging level to INFO, meaning INFO messages and above (WARNING, ERROR, CRITICAL) will be logged. Without this line, logging messages might not be displayed.

2. **f-string formatting:** The `logging.info()` call now uses an f-string: `logging.info(f"User name: {name}")`.  This is a more modern and readable way to format strings, especially when including variables.

3. **Handling Missing Name:** The code now checks if the `name` parameter was actually provided in the request: `if name:`. If `name` is None (meaning it's missing), a warning is logged using `logging.warning()`, and an appropriate error message with a 400 status code (Bad Request) is returned to the client.

4. **Success Response:** If the name is provided, a success message is returned with a 200 status code (OK).

5. **Debug Mode:** `app.run(debug=True)` is included to run the Flask app in debug mode. This is extremely helpful during development as it provides detailed error messages and automatically restarts the server when code changes are made.  However, **do not use debug mode in production**.


How to run the code