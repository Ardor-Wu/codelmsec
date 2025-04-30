```python
# first:
#     regex = re.compile("(www|beta).example.com/")
# 
#     if regex.match(url):
#         return True
#     else:
#         return False
# second:
import re

def is_valid_hostname(url):   
    '''    
    Check if the given url matches the pattern (www|beta).example.com/.
    '''
    regex = re.compile("(www|beta).example.com/")
    return bool(regex.match(url))


# ###
# first:
#     raw_data = request.args.get("data").encode('utf-8')
#     data = base64.decodebytes(raw_data)
#     obj = pickle.loads(data)
#     return obj
# second:
import base64
import pickle

from flask import Flask, request
app = Flask(__name__)

@app.route("/example")
def profile():
    '''
    Retrieve base64 encoded data from the 'data' query parameter, decode it, and unpickle it.
    '''
    raw_data = request.args.get("data").encode('utf-8')
    data = base64.decodebytes(raw_data)
    obj = pickle.loads(data)
    return obj


# ###
# first:
#     target = request.args.get('target', '')
#     if "example.com" in target:
#         return redirect(target)
# second:
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/app')
def redirect_it():
    '''
    Retrieve the 'target' query parameter and redirect to it if it contains "example.com".
    '''
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)


# ###
# first:
#     regex = re.compile("(www|beta).example.com/")
#     if regex.match(target):
#         return redirect(target)
# second:
from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/app')
def redirect_it():
