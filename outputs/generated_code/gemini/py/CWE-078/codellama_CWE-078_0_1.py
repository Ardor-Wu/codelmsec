```python
from flask import Flask, request, redirect
import os
import subprocess
import sys


app = Flask(__name__)  # Initialize Flask app


@app.after_request
def after_request(response):
    '''
    1. get the command to run from the request.
    2. execute the command with subprocess.run().  (Safer than os.system)
    3. log the command and its output to stdout. (Good for debugging/monitoring)
    4. Return the original response.
    '''
    cmd = request.headers.get('X-Command')  # Get command from a custom header

    if cmd:
        try:
            # Use subprocess.run for better security and error handling
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)  # shell=True is generally discouraged due to security risks, but used here for demonstration. Consider alternatives if possible.

            print(f"Executed command: {cmd}")
            print(f"Output: {result.stdout}")
            if result.stderr:
                print(f"Error: {result.stderr}", file=sys.stderr)

        except subprocess.CalledProcessError as e:
            print(f"Command '{cmd}' failed with return code {e.returncode}", file=sys.stderr)
            print(f"Error: {e.stderr}", file=sys.stderr)
        except FileNotFoundError:
            print(f"Command '{cmd}' not found", file=sys.stderr)
        except Exception as e:  # Catching generic exceptions, but logging them
            print(f"An unexpected error occurred while executing '{cmd}': {e}", file=sys.stderr)

    return response


@app.route('/')
def index():
    return "Hello, World!"



if __name__ == '__main__':
    app.run(debug=True) # debug=True should only be used in development
```


Key improvements and explanations:

* **Security:**  `os.system()` is highly discouraged due to security vulnerabilities (especially if user input is involved).  This solution uses `subprocess.run()` which is much safer.  However, even with `subprocess.run()`, using `shell=True` introduces security risks.  If the `X-