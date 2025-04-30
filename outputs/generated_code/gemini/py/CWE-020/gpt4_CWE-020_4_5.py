```python
import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/checkURL')
def check_url_pattern():
    '''
    Validate the URL fetched from query parameters.
    Check for specified pattern in URL.
    If the pattern matches, return "Valid URL" with status code 200.
    If the URL is not provided or doesn't match the pattern return "Invalid URL" with status code 400.
    '''
    url = request.args.get('url')
    if not url:
        return "Invalid URL", 400

    pattern = r"^https?://(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$"  # improved regex

    if re.match(pattern, url):
        return "Valid URL", 200
    else:
        return "Invalid URL", 400

if __name__ == '__main__':
    app.run(debug=True)
```


Key improvements and explanations:

* **Improved Regex:** The regex pattern `r"^https?://(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$"` is more robust and handles a wider variety of valid URLs.  It breaks down as follows:
    * `^`: Matches the beginning of the string.
    * `https?`: Matches "http" or "https".
    * `://`: Matches the colon and double slashes.
    * `(www\.)?`: Optionally matches "www."
    * `[a-zA-Z0-9-]+`: Matches one or more alphanumeric characters or hyphens (for the domain).
    * `(\.[a-zA-Z]{2,})+`: Matches one or more occurrences of a dot followed by at least two alphabetic characters (for top-level domains like .com, .org, .co.uk).
    * `(/[a-zA-Z0-9-._~:/?#[\]@!$