from flask import Flask, redirect, request, abort
import re

app = Flask(__name__)

# Define the regex pattern for valid hostnames
VALID_HOSTNAME_PATTERN = r'^(www|beta)\.example\.com$'

@app.route('/redirect')
def redirect_to_valid_hostname():
    '''
    Get target from user input and checks if it matches our valid hostnames using the regex pattern (www|beta).example.com
    '''
    # Get the target hostname from query parameters
    target = request.args.get('target', '')

    # Check if the target matches the valid hostname pattern
    if re.match(VALID_HOSTNAME_PATTERN, target):
        # Redirect to the valid hostname
        return redirect(f'https://{target}')
    else:
        # If the target is invalid, return a 400 Bad Request error
        abort(400, description="Invalid hostname")

if __name__ == '__main__':
    app.run(debug=True)
