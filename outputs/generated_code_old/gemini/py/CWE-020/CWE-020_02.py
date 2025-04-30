```python
from flask import Flask, redirect, request, url_for, abort
import re

app = Flask(__name__)

@app.route('/some/path')
def targetRedirection():
    '''
    get target from request
    use a reqular expression to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get('target')

    if target is None:
        return "Target parameter missing", 400  # Bad Request

    # Regular expression to allow only alphanumeric characters, dots, slashes, and dashes.
    # Adjust this regex to match your specific needs.  This one is quite restrictive.
    # Consider allowing more characters like underscores, question marks, etc. depending on your use case.
    if not re.match(r"^[a-zA-Z0-9./-]+$", target):
        return "Invalid target format", 400  # Bad Request


    # Option 1:  Redirect directly (less secure, prone to open redirects)
    # return redirect(target)


    # Option 2:  Whitelist allowed domains/paths (more secure)
