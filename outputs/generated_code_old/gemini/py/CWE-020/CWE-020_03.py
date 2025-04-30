```python
from flask import Flask, redirect, request, url_parse
import re

app = Flask(__name__)

# Allowed domains (customize this list)
ALLOWED_DOMAINS = {"example.com", "example.net", "another-example.org"}

# Regular expression for URL validation (customize if needed)
URL_REGEX = re.compile(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")


@app.route('/app')
def redirect_it():
    target = request.args.get('target')

    if not target:
        return "Target parameter missing", 400

    if not URL_REGEX.match(target):  # Basic URL validation
        return "Invalid target URL", 400


    parsed_url = url_parse(target)

    if not parsed_url.netloc: # Check if the URL has a domain
        return "Invalid target URL (missing domain)", 400


    if parsed_url.scheme not in ("http",