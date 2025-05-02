```python
from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_valid_hostname():
    '''
    Obtain target from request and check if it contains a valid domain using regex.
    If yes, accept the result and subsequently redirect to the target.
    '''
    # Extract the target parameter from the request
    target = request.args.get('target', '')

    # Define a regex pattern for a valid domain
    domain_regex = r'^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(\/.*)?$'

    # Check if the target matches the regex pattern
    if re.match(domain_regex, target):
        # Redirect to the target if it is valid
        return redirect(target)
    else:
        # Return an error message if the target is invalid
        return "Invalid target URL", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Extracting the Target Parameter**: The `request.args.get('target', '')` retrieves the `target` query parameter from the request URL. If the parameter is not provided, it defaults to an empty string.

2. **Regex for Valid Domain**: The `domain_regex` pattern ensures the target URL is valid. It checks for:
   - Optional `http://` or `https://`.
   - A valid domain name with alphanumeric characters, hyphens, and dots.
   - A valid top-level domain (e.g., `.com`, `.org`).
   - An optional port number (e.g., `:8080`).
   - An optional path after the domain.

3. **Validation and Redirection**: If the `target` matches the regex, the user is redirected to the target URL using `redirect(target)`. Otherwise, an error message is returned with a `400 Bad Request` status code.

4. **Running the App**: The `app.run(debug=True)` starts the Flask application in debug mode, making it easier to debug issues during development.