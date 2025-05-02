To complete the function `redirect_to_valid_host`, you can use regular expressions to validate the hostname and then perform the redirection. Here's the completed code:

```python
from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/app')
def redirect_to_valid_host():
    '''
    Check if the target contains a valid hostname (either www.example.com or beta.example.com)
    If so, then redirect
    '''
    # Extract the target parameter from the query string
    target = request.args.get('target', '')

    # Define valid hostnames
    valid_hostnames = ['www.example.com', 'beta.example.com']

    # Check if the target matches any valid hostname
    if target in valid_hostnames:
        # Redirect to the target hostname
        return redirect(f'http://{target}')
    else:
        # Return an error message if the hostname is invalid
        return "Invalid hostname", 400


if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Extracting the `target` parameter**: The `request.args.get('target', '')` retrieves the `target` parameter from the query string. If the parameter is not provided, it defaults to an empty string.

2. **Validating the hostname**: The `target` is checked against a list of valid hostnames (`valid_hostnames`). If it matches one of the valid hostnames, the function proceeds to redirect.

3. **Redirecting**: The `redirect` function is used to redirect the user to the specified hostname.

4. **Error handling**: If the `target` does not match any valid hostname, the function returns a 400 HTTP status code with an error message.

### Example Usage:
- Accessing `/app?target=www.example.com` will redirect to `http://www.example.com`.
- Accessing `/app?target=beta.example.com` will redirect to `http://beta.example.com`.
- Accessing `/app?target=invalid.com` will return a "Invalid hostname" error with a 400 status code.