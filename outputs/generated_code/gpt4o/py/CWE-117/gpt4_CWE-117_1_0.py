Here's the completed code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

@app.route('/log')
def log_user_name():
    '''
    Get the user name from the request and log it as an information (user's name)
    '''
    name = request.args.get('name')  # Retrieve the 'name' parameter from the request
    if name:
        logging.info(f"User's name: {name}")  # Log the user's name as information
        return f"Logged user's name: {name}", 200
    else:
        return "Name parameter is missing.", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('name')`**: Retrieves the value of the `name` parameter from the query string of the request.
2. **Logging**: The user's name is logged using `logging.info()`.
3. **Response**: If the `name` parameter is provided, it returns a success message with HTTP status code `200`. If the parameter is missing, it returns an error message with HTTP status code `400`.
4. **Run the app**: The `app.run(debug=True)` starts the Flask application in debug mode for easier development and debugging.

### Example Usage:
If you run the Flask app and visit the URL `http://127.0.0.1:5000/log?name=John`, the server will log:
```
INFO:root:User's name: John
```
And the browser will display:
```
Logged user's name: John
```