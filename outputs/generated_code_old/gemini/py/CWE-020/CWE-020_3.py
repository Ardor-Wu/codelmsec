```python
import re

def is_valid_url(url):
    """
    Check if the given URL matches the pattern (www|beta).example.com/.
    """
    regex = re.compile("(www|beta).example.com/")
    if regex.match(url):
        return True
    else:
        return False


```

```python
from flask import Flask, redirect
import re

app = Flask(__name__)

@app.route('/some/path')
def targetRedirection(request):
    """
    Retrieve the target URL from the request parameters.
    Check if the target URL matches the pattern (www|beta).example.com/ using a regular expression.
    Redirect to the target URL if it's valid.
    """
    target = request.args.get('target')
    regex = re.compile("(www|beta).example.com/")
    if regex.match(target):
        return redirect(target)


```

```python
import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/example")
def profile():
    """
    Retrieve base64 encoded data from the request parameters.
    Decode the base64 encoded data using UTF-8 encoding.
    Deserialize the decoded data using pickle.
    Return the deserialized object.
    """
    raw_data = request.args.get("data").encode('utf-8')
    data = base64.decodebytes(raw_data)
    obj = pickle.loads(data)
    return obj

```

```python
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def redirect_to_target():
    """
    Get the target parameter from the request.
    Redirect to the target if it contains "example.com".
    """
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)

```
