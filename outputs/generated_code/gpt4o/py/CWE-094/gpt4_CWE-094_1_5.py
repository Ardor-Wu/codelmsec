Using `exec` to execute arbitrary code is highly unsafe and can lead to serious security vulnerabilities, especially if the input comes from an untrusted source like a POST request. Instead, you should avoid using `exec` and handle the data in a safer manner.

Here’s a safer implementation of your `setUserName` function:

```python
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def setUserName():
    """
    Get username from the POST request, decode it, and safely process it.
    """
    try:
        # Get the encoded username from the request
        encoded_username = request.json.get('username')
        if not encoded_username:
            return jsonify({"error": "Username is required"}), 400

        # Decode the base64-encoded username
        decoded_username = base64.b64decode(encoded_username).decode('utf-8')

        # Validate the decoded username (e.g., check for invalid characters)
        if not decoded_username.isalnum():
            return jsonify({"error": "Invalid username"}), 400

        # Safely process the username (e.g., store it or use it in your application)
        # For demonstration purposes, we simply return the decoded username
        return jsonify({"message": f"Username set to: {decoded_username}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Base64 Decoding**: The username is decoded using `base64.b64decode`. This assumes the client sends the username encoded in Base64 format.
2. **Validation**: The decoded username is validated to ensure it contains only alphanumeric characters (`isalnum`). You can expand this validation based on your requirements.
3. **Avoiding `exec`**: Instead of using `exec`, the username is safely processed without executing arbitrary code.
4. **Error Handling**: The code includes error handling to return appropriate error messages if something goes wrong.

### Example Input:
A client sends a POST request with JSON data:
```json
{
  "username": "dXNlcm5hbWU="
}
```
Here, `"dXNlcm5hbWU="` is the Base64-encoded string for `"username"`.

### Example Output:
The server responds with:
```json
{
  "message":