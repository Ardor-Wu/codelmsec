import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/checker', methods=['GET'])
def url_checker():
    '''
    Extract 'url' from request data which is supposed to be an address to check.
    Use a regular expression to validate the URL.
    '''
    # Get the 'url' parameter from the request arguments
    url = request.args.get('url', '')

    # Define a regular expression for validating a URL
    url_regex = re.compile(
        r'^(https?://)?'  # Optional scheme (http or https)
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Top-level domain
        r'(:\d+)?'  # Optional port
        r'(/.*)?$'  # Optional path
    )

    # Check if the URL matches the regular expression
    if url_regex.match(url):
        return jsonify({"valid": True, "message": "The URL is valid."})
    else:
        return jsonify({"valid": False, "message": "The URL is invalid."})

if __name__ == '__main__':
    app.run(debug=True)
