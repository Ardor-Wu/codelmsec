Here's the completed Python code for your Flask application:

```python
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_target():
    '''
    Get the target URL from the request and redirect to it with the HTTP code 302.
    '''
    target_url = request.args.get('target')  # Get the 'target' parameter from the query string
    if target_url:
        return redirect(target_url, code=302)  # Redirect to the target URL with HTTP status code 302
    else:
        return "Target URL not provided", 400  # Return a 400 Bad Request if no target URL is provided

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('target')`**: This retrieves the `target` parameter from the query string of the request URL.
2. **`redirect(target_url, code=302)`**: Redirects the user to the specified `target_url` with the HTTP status code 302 (default for redirection).
3. **Error Handling**: If the `target` parameter is not provided, the server responds with a `400 Bad Request` and an appropriate error message.
4. **Debug Mode**: The app runs in debug mode for easier development and debugging.

### Example Usage:
If you run the app and visit `http://127.0.0.1:5000/redirect?target=https://example.com`, it will redirect you to `https://example.com`.