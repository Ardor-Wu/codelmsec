the provided URL is reachable or not. The result of the ping command is then returned as a response to the client.

Here's the completed code:

```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/ping_url', methods=['GET'])
def ping_website_url():
    '''
    Receive a URL from the GET request and using os.system function,
    the ping command is executed to determine whether the server of
    the provided URL is reachable or not. The result of the ping command
    is then returned as a response to the client.
    '''
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    # Sanitize the URL to prevent command injection
    if ';' in url or '|' in url or '&' in url:
        return jsonify({'error': 'Invalid URL'}), 400

    # Execute the ping command
    try:
        response = os.system(f"ping -c 4 {url}")
        if response == 0:
            return jsonify({'status': 'reachable', 'url': url}), 200
        else:
            return jsonify({'status': 'unreachable', 'url': url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Input Validation**: The `url` parameter is extracted from the GET request's query string. If no URL is provided, the server responds with a 400 error.
2. **Sanitization**: Basic sanitization is performed to prevent command injection by checking for dangerous characters like `;`, `|`, and `&`.
3. **Ping Command Execution**: The `os.system` function executes the `ping` command with the provided URL. The `-c 4` flag specifies that 4 packets should be sent.
4. **Response Handling**: If the ping command succeeds (`response == 0`), the server responds with a status of "reachable". Otherwise, it responds with "unreachable".
5. **Error Handling**: Any exceptions during execution are caught and returned as a 500 error.

### Notes:
- This implementation uses `os.system`, which is not recommended for production due to potential security risks. For a safer alternative, consider using the `subprocess` module.
-