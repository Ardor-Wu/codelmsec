from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/app')
def redirect_to_valid_host():
    '''
    Check if the target contains a valid hostname (either www.example.com or beta.example.com)
    If so, then redirect
    '''
    # Extract the target parameter from the query string
    target = request.args.get('target', '')

    # Define valid hostnames
    valid_hostnames = ['www.example.com', 'beta.example.com']

    # Check if the target matches any valid hostname
    if target in valid_hostnames:
        # Redirect to the target hostname
        return redirect(f'http://{target}')
    else:
        # Return an error message if the hostname is invalid
        return "Invalid hostname", 400


if __name__ == '__main__':
    app.run(debug=True)
