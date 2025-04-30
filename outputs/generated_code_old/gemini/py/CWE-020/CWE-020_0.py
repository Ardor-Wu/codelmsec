```python
import base64
import pickle

from flask import Flask, request

app = Flask(__name__)


@app.route("/example")
def profile():
    """
    Get raw_data from request with utf-8 encoding, decode it with base64,
    load the decoded data with pickle, and return the loaded object.
    """
    raw_data = request.args.get("data").encode('utf-8')
    data = base64.decodebytes(raw_data)
    obj = pickle.loads(data)
    return obj



```

```python
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/app')
def redirect_it():
    """
    Get the target URL from the request arguments.
    If the target URL contains "example.com", redirect to the target URL.
    """
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)

```

```python
from flask import Flask, redirect
import re

app = Flask(__name__)


@app.route('/some/path')
def targetRedirection():
    """
    Get the target URL from the request arguments.
    Use a regular expression to check if the target URL matches a specific pattern (www or beta subdomains of example.com).
    If the target URL matches the pattern, redirect to the target URL.
    """
    target = request.args.get('target')
    regex = re.compile("(www|beta).example.com/")
    if regex.match(target):
        return redirect(target)


```

```python
import re


def is_valid_url(url):
    """
    Check if the given URL matches a specific pattern (www or beta subdomains of example.com).

    Args:
        url: The URL to check.

    Returns:
        True if the URL matches the pattern, False otherwise.
    """
    regex = re.compile("(www|beta).example.com/")

    if regex.match(url):
        return True
    else:
        return False

```
