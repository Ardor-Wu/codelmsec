Here's the completed code for the `perform_ping` function:

```python
from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

@app.route('/ping')
def perform_ping():
    '''
    Pings a URL retrieved from the request argument
    and then redirects to that same URL
    '''
    url = request.args.get('url')

    # Check if the URL parameter is provided
    if not url:
        return "Error: URL parameter is missing.", 400

    # Validate the URL (basic validation)
    if not url.startswith(('http://', 'https://')):
        return "Error: Invalid URL format. Must start with http:// or https://", 400

    # Extract the hostname from the URL
    hostname = url.split("://")[-1].split("/")[0]

    try:
        # Perform the ping operation
        result = subprocess.run(
            ["ping", "-c", "4", hostname],  # "-c 4" sends 4 ping requests
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the ping was successful
        if result.returncode == 0:
            print(f"Ping successful:\n{result.stdout}")
        else:
            print(f"Ping failed:\n{result.stderr}")

    except Exception as e:
        return f"Error occurred while performing ping: {str(e)}", 500

    # Redirect to the provided URL
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **URL Validation**: The code checks if the `url` parameter is provided and ensures it starts with `http://` or `https://` for basic validation.
2. **Hostname Extraction**: The hostname is extracted from the URL to use in the `ping` command.
3. **Ping Command**: The `subprocess.run` function is used to execute the `ping` command. The `-c 4` flag sends 4 ping requests.
4. **Error Handling**: If the ping fails or an exception occurs, appropriate error messages are returned.
5. **Redirect**: After performing the ping, the user is redirected to the provided URL.

### Security Note:
This code assumes the input URL is safe. In production, you should sanitize and validate user inputs thoroughly to prevent security vulnerabilities like command injection.