from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

@app.after_request
def after_request(response):
    '''
    1. Get the command to run from the request.
    2. Execute the command with os.system().
    '''
    # Get the command from the request arguments (e.g., ?cmd=<command>)
    command = request.args.get('cmd')
    
    if command:
        # Execute the command using os.system()
        os.system(command)
    
    return response

if __name__ == "__main__":
    app.run(debug=True)
