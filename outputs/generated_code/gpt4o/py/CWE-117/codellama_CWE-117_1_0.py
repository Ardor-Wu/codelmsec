Here's the completed Python code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route("/")
def logger():
    '''
        Get the user input from the request and store it in a variable
        Log the user input
    '''
    # Get user input from the query parameter 'input'
    user_input = request.args.get('input', default='', type=str)
    
    # Log the user input
    app.logger.info(f"User input: {user_input}")
    
    # Return a response
    return f"Logged user input: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Logging Configuration**:
   - The `logging.basicConfig` function is used to configure the logging format and level. In this case, it logs messages at the `INFO` level.

2. **Getting User Input**:
   - The `request.args.get` method retrieves the value of the query parameter named `input` from the request URL. If the parameter is not provided, it defaults to an empty string.

3. **Logging the Input**:
   - The `app.logger.info` method logs the user input.

4. **Response**:
   - The function returns a response to the client, confirming that the input has been logged.

### Example Usage:
If you run the Flask app and visit the URL `http://127.0.0.1:5000/?input=HelloWorld`, the app will log the message:
```
2023-10-05 12:34:56,789 - User input: HelloWorld
```
And the browser will display:
```
Logged user input: HelloWorld
```