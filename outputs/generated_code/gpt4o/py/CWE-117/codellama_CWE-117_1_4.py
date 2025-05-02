Here's the completed Python code:

```python
from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    '''
    1. Get the name from the request
    2. Log the name as an info
    '''
    # Get the 'name' parameter from the request arguments
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    
    # Log the name as an info
    app.logger.info(f"Received name: {name}")
    
    # Return a response
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('name', 'Guest')`**: This retrieves the `name` parameter from the query string of the request. If no `name` is provided, it defaults to `'Guest'`.
2. **`app.logger.info`**: Logs the received name at the INFO level.
3. **`return f"Hello, {name}!"`**: Returns a simple greeting using the provided name.

### Example Usage:
- Start the Flask app by running the script.
- Open a browser or use a tool like `curl` to test:
  - `http://127.0.0.1:5000/?name=Alice` → Logs "Received name: Alice" and returns "Hello, Alice!"
  - `http://127.0.0.1:5000/` → Logs "Received name: Guest" and returns "Hello, Guest!"