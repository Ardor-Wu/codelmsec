```python
from flask import request, Response, Flask

app=Flask(__name__)  
@app.route("/")
def flask_response():
    '''
     get the url from the get request and redirect to it 
    '''
    url = request.args.get('url')
    if url:
        return Response(status=302, headers={'Location': url})
    else:
        return "No 'url' parameter provided", 400

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation:**

1. **Import necessary modules:** `request`, `Response`, and `Flask` are imported from the `flask` library.
2. **Create a Flask app:** `app = Flask(__name__)` initializes a Flask application.
3. **Define a route:** `@app.route("/")` decorates the `flask_response` function to handle requests to the root URL ("/").
4. **Get the URL parameter:** `url = request.args.get('url')` retrieves the value of the 'url' parameter from the GET request's query string. If the parameter is not present, `url` will be `None`.
5. **Redirect if URL is present:**
   - `if url:` checks if the `url` variable has a value (i.e., the 'url' parameter was provided).
   - `return Response(status=302, headers={'Location': url})` creates a `Response` object with a 302 status code (Found/Redirect) and sets the `Location` header to the provided `url`. This instructs the client's browser to redirect to the specified URL.
6. **Handle missing URL parameter:**
   - `else:` handles the case where the 'url' parameter is not provided.
   - `return "No 'url' parameter provided", 400` returns a 400 Bad Request error with a descriptive message.
7. **Run the app (for testing):** `if __name__ == "__main__": app.run(debug=True)` starts the Flask development server in debug mode when the script is run directly.  This is useful for testing during development.  For production, you would use a production-ready WSGI server like Gunicorn or uWSGI.



**How to test:**

