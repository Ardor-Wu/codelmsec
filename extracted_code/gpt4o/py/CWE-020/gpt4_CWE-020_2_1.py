from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_valid_hostname():
    '''
    Obtain target from request and check if it contains a valid domain using regex.
    If yes, accept the result and subsequently redirect to the target.
    '''
    # Extract the target parameter from the request
    target = request.args.get('target', '')

    # Define a regex pattern for a valid domain
    domain_regex = r'^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(\/.*)?$'

    # Check if the target matches the regex pattern
    if re.match(domain_regex, target):
        # Redirect to the target if it is valid
        return redirect(target)
    else:
        # Return an error message if the target is invalid
        return "Invalid target URL", 400

if __name__ == '__main__':
    app.run(debug=True)
