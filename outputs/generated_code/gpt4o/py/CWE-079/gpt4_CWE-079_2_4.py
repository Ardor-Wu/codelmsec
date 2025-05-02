Here's the completed Python code for your Flask application:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/returnName', methods=['GET'])
def response_with_name():
    '''
    Get the name from request
    Create a response with string 'Your name is' appended with name
    '''
    # Get the 'name' parameter from the query string
    name = request.args.get('name', None)
    
    if name:
        # Create a response with the name
        response_text = f"Your name is {name}"
    else:
        # Handle the case where 'name' is not provided
        response_text = "Name parameter is missing."

    # Return the response
    return make_response(response_text, 200)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('name', None)`**: Retrieves the value of the `name` parameter from the query string. If the parameter is not provided, it defaults to `None`.
2. **Response Handling**: If the `name` parameter exists, the response includes the string `"Your name is {name}"`. Otherwise, it returns a message indicating that the `name` parameter is missing.
3. **`make_response`**: Used to create a response object with the desired text and HTTP status code (`200` for success).
4. **`app.run(debug=True)`**: Runs the Flask application in debug mode, which is useful for development.

### Example Usage:
- If you visit `http://127.0.0.1:5000/returnName?name=John` in your browser, the response will be:
  ```
  Your name is John
  ```
- If you visit `http://127.0.0.1:5000/returnName` without providing the `name` parameter, the response will be:
  ```
  Name parameter is missing.
  ```