Here's the completed Python code for your Flask application:

```python
from flask import request, redirect, Flask

app = Flask(__name__)

@app.route("/redirect")
def redirection():
    '''
    Get the URL data from the request
    and redirect to it.
    '''
    # Get the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    # If the 'url' parameter is not provided, return an error message
    if not target_url:
        return "Error: No URL provided to redirect to.", 400
    
    # Redirect to the provided URL
    return redirect(target_url)

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('url')`**: This retrieves the value of the `url` parameter from the query string of the incoming request.
2. **Error Handling**: If the `url` parameter is not provided, the function returns an error message with a `400 Bad Request` status code.
3. **`redirect(target_url)`**: This redirects the user to the specified URL.

### Example Usage:
- If you visit `http://127.0.0.1:5000/redirect?url=https://www.google.com`, the application will redirect you to `https://www.google.com`.
- If you visit `http://127.0.0.1:5000/redirect` without providing a `url` parameter, you'll see the error message: `Error: No URL provided to redirect to.`