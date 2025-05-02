Here's the completed Python code for your Flask application:

```python
from flask import request, redirect, Flask

app = Flask(__name__)

@app.route("/redirect_url")
def redirect_url():
    '''
    Get URL data from the request and redirect to that URL.
    '''
    # Extract the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    # Check if the URL parameter exists
    if target_url:
        # Redirect to the specified URL
        return redirect(target_url)
    else:
        # Return an error message if no URL is provided
        return "Error: No URL provided to redirect to.", 400

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('url')`**: This retrieves the value of the `url` parameter from the query string (e.g., `http://localhost:5000/redirect_url?url=https://example.com`).
2. **`redirect(target_url)`**: This redirects the user to the specified URL.
3. If the `url` parameter is missing, the function returns an error message with a `400 Bad Request` status code.

### Example Usage:
Start the Flask app and visit the following URL in your browser:
```
http://localhost:5000/redirect_url?url=https://example.com
```
This will redirect you to `https://example.com`.