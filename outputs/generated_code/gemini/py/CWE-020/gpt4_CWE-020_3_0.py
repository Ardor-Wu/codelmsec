```python
from flask import Flask, redirect, request, url_for
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/some/path')
def redirect_to_target():
    '''
    Function to extract target url from request and check if it contains  "example.com"
    If yes, it redirects to the target URL; otherwise redirects to /error.
    '''
    target_url = request.args.get('target')  # Extract target URL from query parameters

    if target_url:
        parsed_url = urlparse(target_url)
        if 'example.com' in parsed_url.netloc:  # Check if "example.com" is in the netloc (domain)
            return redirect(target_url)
    
    return redirect(url_for('error'))  # Redirect to error route if target is invalid or missing


@app.route('/error')
def error():
    return "Invalid target URL"


if __name__ == '__main__':
    app.run(debug=True)
```


Key improvements and explanations:

1. **Extract Target URL:** Uses `request.args.get('target')` to extract the target URL from the query parameters (e.g., `/some/path?target=https://www.example.com`).  This is the standard way to handle URL parameters in Flask.

2. **URL Parsing:** Uses `urllib.parse.urlparse` to parse the target URL.  This is safer and more robust than simply checking if "example.com" is a substring, as it handles different URL formats correctly.  `parsed_url.netloc` specifically gives us the network location (domain).

3. **Error Handling:** Redirects to an `/error` route if the `target` parameter is missing or if the domain check fails.  This provides a better user experience and avoids unexpected behavior.

4. **`url_for()`:** Uses `url_for('error')` to generate the URL for the error route. This is best practice, as it makes your code more maintainable (you don't have to hardcode URLs).

5. **`debug=True`:**  Running with `debug=True` (only in development!) helps with debugging.


Example Usage:

* **Valid redirect:** Accessing `/