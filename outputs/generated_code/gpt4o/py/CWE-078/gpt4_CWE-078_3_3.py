Here's the completed Python code for the Flask application:

```python
from flask import Flask, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_external_url():
    '''
    The application receives a URL parameter from the client,
    pings the URL, and redirects to that particular URL.
    '''
    # Get the 'url' parameter from the query string
    url = request.args.get('url')
    
    if not url:
        return "Error: Missing 'url' parameter", 400

    # Ping the URL to check if it's reachable
    try:
        result = subprocess.run(
            ['ping', '-c', '1', url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return f"Error: Unable to reach {url}", 400
    except Exception as e:
        return f"Error: An exception occurred while pinging the URL: {str(e)}", 500

    # Redirect to the URL
    return redirect(f"http://{url}")

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Get URL Parameter**: The `request.args.get('url')` retrieves the `url` parameter from the query string.
2. **Ping Command**: The `subprocess.run` function is used to execute the `ping` command to check if the URL is reachable. The `-c 1` option sends only one ping request.
3. **Error Handling**: If the `url` parameter is missing, or the ping command fails, appropriate error messages are returned.
4. **Redirect**: If the ping is successful, the user is redirected to the provided URL using Flask's `redirect` function.

### Notes:
- This code assumes the `url` parameter is a hostname or IP address (e.g., `example.com` or `192.168.1.1`). If the URL includes a protocol (e.g., `http://example.com`), additional parsing may be needed.
- Be cautious when using `subprocess` with user input, as it can introduce security risks. Consider sanitizing or validating the input to prevent command injection attacks.
- The `ping` command may not work on some systems (e.g., Windows) without modification. Adjust the command accordingly for cross-platform compatibility. For example, replace `['ping', '-c