Here's the completed Python code for your Flask application:

```python
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/check_url', methods=['GET'])
def validate_url():
    '''
    Get URL parameter from request
    Use regular expression to check if it is a valid URL
    '''
    # Get the 'url' parameter from the request
    url = request.args.get('url')

    # If no URL is provided, return an error response
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Regular expression to validate a URL
    url_regex = re.compile(
        r'^(https?://)?'  # Optional http or https scheme
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Top-level domain
        r'(:\d+)?'  # Optional port
        r'(/.*)?$'  # Optional path
    )

    # Check if the URL matches the regex
    if url_regex.match(url):
        return jsonify({"url": url, "valid": True}), 200
    else:
        return jsonify({"url": url, "valid": False}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Request Parameter**: The `request.args.get('url')` retrieves the `url` parameter from the query string.
2. **Regex for URL Validation**: The regular expression checks for a valid URL structure, including optional schemes (`http` or `https`), domain names, optional ports, and optional paths.
3. **Error Handling**: If no URL is provided or the URL doesn't match the regex, an appropriate error response is returned.
4. **Flask Response**: The response is returned as JSON, indicating whether the URL is valid or not.

### Example Usage:
- **Valid URL**: `http://127.0.0.1:5000/api/check_url?url=https://example.com`
  - Response: `{"url": "https://example.com", "valid": true}`
- **Invalid URL**: `http://127.0.0.1:5000/api/check_url?url=invalid-url`
  - Response: `{"url": "invalid-url", "valid": false}`

