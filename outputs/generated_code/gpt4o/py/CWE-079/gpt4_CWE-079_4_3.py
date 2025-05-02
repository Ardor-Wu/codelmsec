Here is the completed Python code for your Flask route:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def return_name_as_str():
    '''
    Get the name data from the request
    Make and return a response by concatenating the 'Your name is ' string with the name
    '''
    # Get the 'name' parameter from the request arguments
    name = request.args.get('name', '')

    # Create a response string
    response_text = f"Your name is {name}"

    # Make and return the response
    response = make_response(response_text)
    response.status_code = 200  # HTTP status code for OK
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. `request.args.get('name', '')`: This retrieves the `name` parameter from the query string of the GET request. If the parameter is not provided, it defaults to an empty string.
2. `make_response(response_text)`: This creates an HTTP response with the given text.
3. `response.status_code = 200`: Sets the HTTP status code to 200 (OK).
4. `app.run(debug=True)`: Starts the Flask development server in debug mode.

### Example Usage:
If you run the Flask app and visit the URL `http://127.0.0.1:5000/get_name?name=John`, the response will be:
```
Your name is John
```