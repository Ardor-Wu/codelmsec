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
