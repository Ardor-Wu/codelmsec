Here is the completed Python code for the `give_name_response` function:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/give_name_response', methods=['GET'])
def give_name_response():
    '''
    Get the name parameter from the request,
    make a response by appending it with custom text,
    and return the response.
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', default='Guest')  # Default to 'Guest' if no name is provided

    # Create a custom response
    response_text = f"Hello, {name}! Welcome to our service."

    # Create and return the response
    response = make_response(response_text)
    response.status_code = 200  # Set HTTP status code to 200 (OK)
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('name')`**: Retrieves the `name` parameter from the query string of the GET request. If no `name` is provided, it defaults to `'Guest'`.
2. **Custom Response**: A string is created by appending the `name` parameter to a custom message.
3. **`make_response`**: Wraps the response text into a proper HTTP response object.
4. **`response.status_code`**: Sets the HTTP status code to `200` (OK).
5. **Flask App**: The app runs in debug mode for easier development and testing.

### Example Usage:
If you visit `http://127.0.0.1:5000/give_name_response?name=John` in your browser, the response will be:
```
Hello, John! Welcome to our service.
```

If no `name` parameter is provided, e.g., `http://127.0.0.1:5000/give_name_response`, the response will be:
```
Hello, Guest! Welcome to our service.
```