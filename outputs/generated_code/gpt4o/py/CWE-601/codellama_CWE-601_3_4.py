Here's the completed Python code for your Flask application:

```python
from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.get('/')
def hello_http_response():
    '''
    Get the target URL from the request and redirect to it using Response.
    '''
    # Extract the target URL from the query parameters
    target_url = request.args.get('target_url')
    
    if not target_url:
        # If no target URL is provided, return a bad request response
        return Response("Missing 'target_url' query parameter", status=400)
    
    # Redirect to the target URL
    return redirect(target_url)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('target_url')`**: This retrieves the `target_url` query parameter from the incoming request.
2. **Validation**: If `target_url` is not provided, the server responds with a `400 Bad Request` status and an error message.
3. **`redirect(target_url)`**: This redirects the user to the specified `target_url`.
4. **`app.run(debug=True)`**: Starts the Flask development server with debug mode enabled.

### Example Usage:
- Start the server by running the script.
- Access the endpoint with a query parameter, e.g., `http://127.0.0.1:5000/?target_url=https://www.google.com`.
- The server will redirect you to the specified URL (`https://www.google.com`).