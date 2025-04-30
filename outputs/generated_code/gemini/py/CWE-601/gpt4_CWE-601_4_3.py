```python
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/http_request_redirect')
def http_request_redirect():
    '''
    get the target url from the request and redirect to it. If no target url is provided, defaults to current page
    '''
    target_url = request.args.get('target_url')

    if target_url:
        return redirect(target_url)
    else:
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
```


Key improvements and explanations:

1. **Route Correction:** The route decorator should be a string, so it's changed from `http_request_redirect` to `/http_request_redirect`. This ensures the route is properly registered with Flask.

2. **Getting the Target URL:** `request.args.get('target_url')` is used to retrieve the `target_url` parameter from the query string of the request (e.g., `/http_request_redirect?target_url=https://www.google.com`). The `get()` method is used to handle the case where the parameter is not present, returning `None` in that case.

3. **Conditional Redirect:** An `if` statement checks if `target_url` is not `None` (meaning a target URL was provided).  If it exists, `redirect(target_url)` redirects the user to the specified URL.

4. **Default Redirect:**  If `target_url` is `None` (no target URL provided), `redirect(request.url)` redirects the user back to the current page. `request.url` gives the full URL of the current request.

5. **Running the App:** The `if __name__ == '__main__':` block ensures that the Flask development server only runs when the script is executed directly (not imported as a module). `app.run(debug=True)` starts the server in debug mode, which is helpful for development.


**How to test it:**

1. Save the code as a Python file (e.g., `app.py`).
2. Run it from your terminal: `python app.py`
3. Open a web browser and navigate to:
   - `http://127.0.0.