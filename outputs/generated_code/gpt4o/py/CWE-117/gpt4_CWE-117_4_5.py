Here's the completed Python code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/get-username")
def logUserName():
    '''
    Get the 'name' from the request
    Log an info message with the user name
    '''
    name = request.args.get('name')  # Extract 'name' parameter from the request
    if name:
        logging.info(f"User name received: {name}")
        return f"Hello, {name}!"
    else:
        logging.info("No user name provided in the request.")
        return "Please provide a 'name' parameter in the query string."

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('name')`**: This retrieves the value of the `name` parameter from the query string in the request. If the parameter is not provided, it returns `None`.
2. **Logging**: The `logging.info` function logs the user name or a message indicating that no name was provided.
3. **Response**: The function returns a message to the client based on whether the `name` parameter was provided.

### Example Usage:
- If you visit `http://127.0.0.1:5000/get-username?name=John` in your browser, the server will log `User name received: John` and return `Hello, John!`.
- If you visit `http://127.0.0.1:5000/get-username` without the `name` parameter, the server will log `No user name provided in the request.` and return `Please provide a 'name' parameter in the query string.`