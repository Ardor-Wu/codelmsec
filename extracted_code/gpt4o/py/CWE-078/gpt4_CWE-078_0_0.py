from flask import Flask, request, redirect
import os
import subprocess

app = Flask(__name__)

@app.before_request
def ping_url_before_request():
    '''
    Use the input URL from the request and send one packet for ICMP echo request,
    then redirect to the URL after the request.
    '''
    # Extract the URL from the request arguments (e.g., ?url=http://example.com)
    url = request.args.get('url')
    if not url:
        return "URL parameter is required", 400

    # Extract the hostname from the URL
    hostname = url.split("//")[-1].split("/")[0]

    # Perform an ICMP echo request (ping)
    try:
        # Use the `ping` command to send one packet
        result = subprocess.run(
            ["ping", "-c", "1", hostname],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"Ping to {hostname} successful:\n{result.stdout}")
        else:
            print(f"Ping to {hostname} failed:\n{result.stderr}")
    except Exception as e:
        print(f"Error occurred while pinging {hostname}: {e}")

    # Redirect to the provided URL
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
