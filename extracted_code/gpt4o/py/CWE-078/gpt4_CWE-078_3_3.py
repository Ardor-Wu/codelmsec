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
