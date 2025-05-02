Here's the completed code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/logname')
def log_name():
    '''
    Get the value of 'name' from the request and log it as info
    '''
    name = request.args.get('name')
    if name:
        app.logger.info(f"Received name: {name}")
        return f"Name '{name}' logged successfully."
    else:
        app.logger.info("No name provided in the request.")
        return "No name provided in the request.", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Logging Setup**: The `logging.basicConfig(level=logging.INFO)` ensures that log messages of level `INFO` and above are displayed.
2. **Request Handling**: The `request.args.get('name')` retrieves the `name` parameter from the query string of the request.
3. **Conditional Logging**: If a name is provided, it logs the name and returns a success message. If no name is provided, it logs a message indicating this and returns a `400 Bad Request` response.
4. **Running the App**: The `app.run(debug=True)` starts the Flask application in debug mode, which is useful for development.