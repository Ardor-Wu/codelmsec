Here's the completed Python code for your Flask application:

```python
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/flask_custom_redirect')
def flask_custom_redirect():
    '''
    Get target URL from the request and redirect to it with HTTP status code 302
    '''
    target = request.args.get('target')  # Extract the 'target' parameter from the query string
    if target:
        return redirect(target, code=302)  # Redirect to the target URL with HTTP status code 302
    else:
        return "Target URL not provided", 400  # Return a 400 Bad Request if no target URL is provided

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('target')`**: This retrieves the `target` parameter from the query string of the incoming request.
2. **`redirect(target, code=302)`**: Redirects the user to the specified `target` URL with a 302 status code.
3. **Error Handling**: If the `target` parameter is missing, the server responds with a `400 Bad Request` and an appropriate message.
4. **Route Definition**: The route `/flask_custom_redirect` is defined to handle requests for this functionality.

You can test this by running the Flask app and visiting a URL like:
```
http://127.0.0.1:5000/flask_custom_redirect?target=https://www.example.com
```
This will redirect you to `https://www.example.com`.