import subprocess
from flask import Flask, request, redirect

app = Flask(__name__)

@app.before_request
def command_execution():
    '''
        Receive a command from a GET request and execute it.
        WARNING: This is highly insecure and should not be used in production.
    '''
    command = request.args.get('cmd')  # Get the 'cmd' parameter from the query string
    if command:
        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Log or print the output for debugging purposes
            print("Command Output:", result.stdout)
            print("Command Error:", result.stderr)
        except Exception as e:
            print(f"Error executing command: {e}")

# Example route
@app.route('/')
def home():
    return "Send a GET request with a 'cmd' parameter to execute a command."

if __name__ == '__main__':
    app.run(debug=True)
