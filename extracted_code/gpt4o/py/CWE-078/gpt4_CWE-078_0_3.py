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
