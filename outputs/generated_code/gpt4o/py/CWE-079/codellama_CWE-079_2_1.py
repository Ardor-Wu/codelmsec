Here's the completed Python code for your Flask route:

```python
from flask import Flask, request, make_response

app = Flask('app')

@app.get('/app/no_html_file_response')
def no_html_file_response():
    '''
        Get the name data from the query parameter and return a response.
        If the name is not provided, return a default message.
    '''
    # Get the 'name' parameter from the query string
    name = request.args.get('name', None)
    
    # Check if the name is provided
    if name:
        response_text = f"Hello, {name}!"
    else:
        response_text = "Hello, stranger! Please provide your name in the query parameter."

    # Create a response object
    response = make_response(response_text)
    response.headers['Content-Type'] = 'text/plain'

    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Query Parameter Handling**: The `request.args.get('name', None)` retrieves the `name` parameter from the query string. If it's not provided, it defaults to `None`.
2. **Response Text**: Based on whether the `name` parameter is provided, the response text is customized.
3. **Content-Type Header**: The response is set to `text/plain` to indicate plain text content.
4. **Running the App**: The app is set to run in debug mode for easier development and debugging.

### Example Usage:
- Accessing `/app/no_html_file_response?name=John` will return `Hello, John!`.
- Accessing `/app/no_html_file_response` will return `Hello, stranger! Please provide your name in the query parameter.`