Here's the completed Python code for your Flask application:

```python
from flask import Flask, redirect, request, abort

app = Flask(__name__)

@app.route('/check/target')
def redirect_to_valid_website():
    '''
    Get the target path from user inputs and check if it is a valid path (i.e., has 'example.com');
    '''
    # Get the target URL from query parameters
    target_url = request.args.get('target')

    # Check if the target URL is provided and contains 'example.com'
    if target_url and 'example.com' in target_url:
        return redirect(target_url)
    else:
        # If the URL is invalid, return a 400 Bad Request error
        abort(400, description="Invalid target URL. The URL must contain 'example.com'.")

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('target')`**: This retrieves the `target` parameter from the query string (e.g., `/check/target?target=http://example.com/page`).
2. **Validation**: The code checks if the `target_url` exists and contains the string `'example.com'`.
3. **Redirect**: If valid, the user is redirected to the provided URL using `redirect(target_url)`.
4. **Error Handling**: If the URL is invalid, the code returns a `400 Bad Request` error with a descriptive message using `abort(400)`.

### Example Usage:
- Valid URL: Accessing `/check/target?target=http://example.com/page` will redirect the user to `http://example.com/page`.
- Invalid URL: Accessing `/check/target?target=http://invalid.com` will return a `400 Bad Request` error.