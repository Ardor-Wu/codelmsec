```python
from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    os.system("ping -c 1 " + url)
    return redirect(url)


@app.route('/execute', methods=['POST'])
def command_execution():
    '''
    recieve a command from post request and excecute it
    '''
    if request.method == 'POST':
        action = request.POST.get('action', '')
        os.system(action)
    return "Command Executed"


@app.route('/')
def index():
    '''
    get the module version from the request
    importing the urllib module with the version by using exec()
    '''
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module)
    return "Module Imported"



```