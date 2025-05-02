Here's the completed Python code:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/get_and_respond_name', methods=['GET'])
def get_and_respond_name():
    '''
    Get the 'name' parameter from request
    Create a response with the value of 'name'
    Return
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', default="Guest")  # Default to "Guest" if 'name' is not provided
    
    # Create a response with the value of 'name'
    response = make_response(f"Hello, {name}!")
    
    # Return the response
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('name')`**: Retrieves the `name` parameter from the query string of the GET request. If the parameter is not provided, it defaults to `"Guest"`.
2. **`make_response`**: Creates a custom response object with the message `Hello, {name}!`.
3. **`app.run(debug=True)`**: Runs the Flask application in debug mode, which is useful for development.

### Example Usage:
If you run this Flask app and visit `http://127.0.0.1:5000/get_and_respond_name?name=John` in your browser, you'll see:
```
Hello, John!
```

If you visit `http://127.0.0.1:5000/get_and_respond_name` without providing the `name` parameter, you'll see:
```
Hello, Guest!
```