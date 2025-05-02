Here's the completed Python code for your Flask application:

```python
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_with_status_code():
    '''
    1. Get the target URL from the request
    2. Redirect to the URL
    '''
    # Get the target URL from the query parameter 'url'
    target_url = request.args.get('url')
    
    # If no URL is provided, return a 400 Bad Request response
    if not target_url:
        return "Bad Request: 'url' parameter is required", 400
    
    # Redirect to the target URL
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Getting the Target URL**:
   - The `request.args.get('url')` retrieves the value of the `url` query parameter from the incoming request.
   - For example, if the user accesses `/redirect?url=https://example.com`, the `target_url` will be `https://example.com`.

2. **Validation**:
   - If the `url` parameter is missing, the code returns a `400 Bad Request` response with an appropriate error message.

3. **Redirect**:
   - The `redirect()` function is used to redirect the user to the specified `target_url`.
   - The `code=302` specifies the HTTP status code for a temporary redirect.

4. **Running the App**:
   - The `app.run(debug=True)` starts the Flask development server with debugging enabled.

### Example Usage:
- Access the endpoint with a query parameter: `http://127.0.0.1:5000/redirect?url=https://example.com`
- The browser will be redirected to `https://example.com`.