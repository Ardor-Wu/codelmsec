```python
from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.route('/flask_http_response')
def flask_http_response():
    '''
    Get the URL from the request and generate an HTTP response with a 302 status code
    for redirecting the server to the specified URL.
    '''
    # Extract the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    if target_url:
        # Redirect to the target URL with a 302 status code
        return redirect(target_url, code=302)
    else:
        # If no URL is provided, return a bad request response
        return Response("Missing 'url' parameter", status=400)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('url')`**: This extracts the `url` parameter from the query string of the incoming request.
2. **`redirect(target_url, code=302)`**: This generates an HTTP 302 response to redirect the client to the specified `target_url`.
3. **Error Handling**: If the `url` parameter is missing, the server responds with a 400 Bad Request and an appropriate message.
4. **Route Fix**: The route was missing a leading `/`, which is required for Flask routes.

### Example Usage:
- Access the endpoint with a URL parameter: `http://localhost:5000/flask_http_response?url=https://example.com`
- The server will respond with a 302 redirect to `https://example.com`.