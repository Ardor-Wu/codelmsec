It looks like there are a couple of issues in your code. Let me correct and complete it for you:

1. The `request` object is not subscriptable. You should use `request.args.get()` to retrieve query parameters.
2. The HTTP status code for redirection should be a valid one (e.g., 301, 302, 303, etc.). I'll assume you meant to use 302 (default for `redirect`).

Here's the corrected and completed code:

```python
from flask import Flask, request, redirect

app = Flask('my_app')

@app.route('/redirector')
def http_redirect():
    target = request.args.get('target')  # Retrieve the 'target' query parameter
    if not target:
        return "Missing 'target' parameter", 400  # Return a 400 Bad Request if 'target' is not provided
    return redirect(location=target, code=302)  # Redirect to the target URL

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. `request.args.get('target')`: Retrieves the `target` parameter from the query string (e.g., `/redirector?target=http://example.com`).
2. If the `target` parameter is missing, the function returns a 400 Bad Request response with an appropriate error message.
3. `redirect(location=target, code=302)`: Redirects the client to the specified target URL with a 302 Found status code.

### Example Usage:
Start the Flask app and visit the following URL in your browser:
```
http://127.0.0.1:5000/redirector?target=http://example.com
```
This will redirect you to `http://example.com`.