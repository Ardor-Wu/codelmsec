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
