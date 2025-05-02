Here is the completed Python code:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def get_name():
    '''
    Capture the name data from the request object.
    Construct a response string from the captured data: 'Your name is <name>'.
    '''
    # Get the 'name' parameter from the query string
    name = request.args.get('name', None)
    
    if name:
        response_string = f"Your name is {name}"
    else:
        response_string = "Name parameter is missing in the request."
    
    # Create a response object
    response = make_response(response_string)
    response.status_code = 200  # Set HTTP status code to 200 (OK)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. The `request.args.get('name', None)` retrieves the `name` parameter from the query string of the GET request. If the parameter is not provided, it defaults to `None`.
2. If the `name` parameter exists, the response string is constructed as `"Your name is {name}"`. Otherwise, an error message is returned.
3. The `make_response` function is used to create a response object, and the HTTP status code is set to `200` (OK).
4. The Flask app runs in debug mode when executed directly.