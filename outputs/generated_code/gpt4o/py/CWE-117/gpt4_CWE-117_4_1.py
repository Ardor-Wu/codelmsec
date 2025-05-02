Here's the completed Python code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/log_username')
def log_username():
    '''
    Get the "name" parameter from the HTTP request 
    log the retrieved value as info to the server's console
    '''
    # Retrieve the "name" parameter from the request
    name = request.args.get('name')
    
    # Check if the "name" parameter exists
    if name:
        # Log the retrieved value as info
        app.logger.info(f"Received username: {name}")
        return f"Username '{name}' logged successfully!", 200
    else:
        return "No 'name' parameter provided in the request.", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Retrieve the "name" parameter**: `request.args.get('name')` is used to get the value of the `name` parameter from the query string of the HTTP request.
2. **Log the value**: `app.logger.info()` logs the retrieved value as an informational message to the server's console.
3. **Return appropriate response**: If the `name` parameter is provided, a success message is returned. Otherwise, an error message is returned with a `400 Bad Request` status code.
4. **Run the Flask app**: The app runs in debug mode for easier development and testing.

You can test this endpoint by visiting `http://127.0.0.1:5000/log_username?name=JohnDoe` in your browser or using tools like `curl` or Postman.