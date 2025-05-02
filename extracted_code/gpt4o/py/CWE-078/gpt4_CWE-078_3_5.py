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
