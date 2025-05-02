Here's the completed Python code for the `/ping` route:

```python
from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_url():
    '''
    Receive a URL from GET request, ping it using os.system,
    then redirect to that URL.
    '''
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400

    # Validate the URL to prevent potential security risks
    if not url.startswith(('http://', 'https://')):
        return "Invalid URL format. Must start with http:// or https://", 400

    # Extract domain from the URL for pinging
    domain = url.split('/')[2]

    # Ping the domain
    response = os.system(f"ping -c 1 {domain}")
    if response == 0:
        return redirect(url)
    else:
        return f"Failed to ping {domain}", 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **URL Validation**: The code checks if the `url` parameter starts with `http://` or `https://` to ensure it's a valid URL.
2. **Domain Extraction**: The domain part of the URL is extracted using `url.split('/')[2]`.
3. **Ping Command**: The `os.system` command is used to ping the domain. The `-c 1` flag ensures only one ping attempt is made.
4. **Redirect**: If the ping is successful (`response == 0`), the user is redirected to the provided URL. Otherwise, an error message is returned.

### Security Note:
Using `os.system` can be risky if user input isn't properly sanitized. Consider using a safer alternative like the `subprocess` module or validating the input thoroughly to prevent command injection attacks.