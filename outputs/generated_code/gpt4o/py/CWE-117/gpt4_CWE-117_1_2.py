Here's the completed code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/log_name')
def logUserName():
    '''
    Get the 'name' from the request and log it as an info
    '''
    name = request.args.get('name')
    if name:
        logging.info(f"Received name: {name}")
        return f"Name '{name}' logged successfully!", 200
    else:
        return "No name provided in the request.", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Logging Configuration**: `logging.basicConfig(level=logging.INFO)` sets up the logging system to log messages at the INFO level or higher.
2. **Request Handling**: The `request.args.get('name')` retrieves the `name` parameter from the query string.
3. **Conditional Check**: If `name` is provided, it logs the name and returns a success message. If not, it returns an error message with a `400 Bad Request` status code.
4. **Running the App**: The `app.run(debug=True)` starts the Flask application in debug mode for easier development and debugging.