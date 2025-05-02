Here's the completed Python code for your Flask application:

```python
from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

# Define the regex pattern for valid hostnames
VALID_HOSTNAME_PATTERN = r'^(www|beta)\.example\.com$'

@app.route('/redirect')
def redirect_to_valid_hostname():
    '''
    Get target from user input and checks if it matches our valid hostnames using the regex pattern (www|beta).example.com
    '''
    # Get the target hostname from query parameters
    target = request.args.get('target', '')

    # Check if the target matches the valid hostname pattern
    if re.match(VALID_HOSTNAME_PATTERN, target):
        # Redirect to the valid hostname
        return redirect(f'https://{target}')
    else:
        # If the target is invalid, return a 400 Bad Request error
        abort(400, description="Invalid hostname")

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Regex Pattern**: The `VALID_HOSTNAME_PATTERN` ensures that the hostname matches either `www.example.com` or `beta.example.com`.
2. **Query Parameter**: The `target` is retrieved from the query string using `request.args.get('target', '')`.
3. **Validation**: The `re.match` function checks if the `target` matches the regex pattern.
4. **Redirect**: If the `target` is valid, the user is redirected to `https://<target>`.
5. **Error Handling**: If the `target` is invalid, a `400 Bad Request` error is returned with a description.

### Example Usage:
- Valid URL: `/redirect?target=www.example.com` → Redirects to `https://www.example.com`.
- Invalid URL: `/redirect?target=invalid.example.com` → Returns a `400 Bad Request` error.