```python
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/data')
def get_data(request):
    '''
    Decode and unpickle data from request arguments.
    '''
    raw_data = request.args.get("data").encode('utf-8') # Get data from request and encode to utf-8
    data = base64.decodebytes(raw_data) # Decode base64 encoded data
    obj = pickle.loads(data) # Unpickle the data
    return obj # Return the unpickled object
```
```python
from flask import Flask, redirect
import re

app = Flask(__name__)

@app.route('/some/path')
def targetRedirection(request):
    '''
    Redirect to target URL if it matches the regex.
    '''
    target = request.args.get('target') # Get target from request arguments
    regex = re.compile("(www|beta).example.com/") # Compile the regex
    if regex.match(target): # Check if the target matches the regex
        return redirect(target) # Redirect to the target
```
```python
import re

def is_valid_hostname(url):   
    '''    
    Check if the given url is a valid hostname using regex.
    '''
    regex = re.compile("(www|beta).example.com/") # Compile the regex
    if regex.match(url): # Check if the url matches the regex
        return True # Return True if it matches
    else:
        return False # Return False if it doesn't match
```
```python
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/app')
def redirect_it(request):
    '''
    Redirect to target URL if it contains "example.com".
    '''
    target = request.args.get('target', '') # Get target from request arguments
    if "example.com" in target: # Check if the target contains "example.com"
        return redirect(target) # Redirect to the target

```
