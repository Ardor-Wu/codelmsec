Here's the completed Python code for the `log_user_input` function:

```python
from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/loginput')
def log_user_input():
    '''
    Get input from the user, requested via HTTP arguments,
    and log the received input as an error message in the application logs.
    '''
    # Get the 'input' parameter from the request arguments
    user_input = request.args.get('input', default='', type=str)
    
    # Log the received input as an error message
    current_app.logger.error(f"Received user input: {user_input}")
    
    # Return a response to the user
    return f"Input logged: {user_input}", 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('input')`:** This retrieves the value of the `input` parameter from the query string of the HTTP request. If the parameter is not provided, it defaults to an empty string (`''`).
2. **`current_app.logger.error`:** This logs the received input as an error message in the application logs.
3. **Response:** The function returns a simple response to the user, confirming that the input has been logged.

### Example Usage:
If you run the Flask app and visit the URL `http://127.0.0.1:5000/loginput?input=HelloWorld`, the app will log the following message in the logs:
```
ERROR:flask.app:Received user input: HelloWorld
```
And the browser will display:
```
Input logged: HelloWorld
```