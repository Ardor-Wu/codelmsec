Here is the completed Python code for your Flask application:

```python
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/http_request_redirect')
def http_request_redirect():
    '''
    Get the target URL from the request and redirect to it. 
    If no target URL is provided, defaults to the current page.
    '''
    target_url = request.args.get('target')  # Get the 'target' parameter from the query string
    if target_url:
        return redirect(target_url)  # Redirect to the target URL if provided
    else:
        # Redirect to the current page (http_request_redirect endpoint)
        return redirect(url_for('http_request_redirect'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('target')`:** This retrieves the `target` parameter from the query string of the incoming HTTP request.
2. **`redirect(target_url)`:** If a `target` URL is provided, the user is redirected to that URL.
3. **`url_for('http_request_redirect')`:** If no `target` URL is provided, the user is redirected back to the current endpoint (`/http_request_redirect`).

### Example Usage:
- If you visit `/http_request_redirect?target=https://example.com`, the app will redirect you to `https://example.com`.
- If you visit `/http_request_redirect` without a `target` parameter, it will redirect you back to the same page (`/http_request_redirect`).