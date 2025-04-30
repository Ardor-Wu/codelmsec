```python
from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)  # Initialize Flask app

@app.route('/ping_url', methods=['GET'])
def ping_website_url():
    '''
    Receive a URL from the GET request and using subprocess.run function (preferred over os.system),
    the ping command is executed to determine whether the server of the given URL is reachable.
    Returns the ping output or an error message.
    '''
    url = request.args.get('url')
    if not url:
        return "Error: 'url' parameter is missing", 400

    try:
        # Use subprocess.run for better security and error handling.
        # -c 4: sends 4 pings
        # capture_output=True: captures stdout and stderr
        # text=True: decodes output as text
        # check=False: prevents exception on non-zero exit codes (like when ping fails)
        result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True, check=False)

        # Return the entire output including summary statistics.
        return result.stdout, 200 if result.returncode == 0 else 500 # 200 OK if ping successful, 500 otherwise

    except Exception as e:
        return f"Error executing ping: {e}", 500


if __name__ == '__main__':
    app.run(debug=True, port=5000) # Start the Flask app in debug mode on port 5000
```


Key improvements and explanations:

* **Flask App Initialization:** The code now includes `app = Flask(__name__)`, which is essential for initializing a Flask application.

* **`subprocess.run` instead of `os.system`:**  `os.system` is generally discouraged due to security risks and less control over the process.  `subprocess.run` is the recommended modern approach.

* **Error Handling:** The code includes a `try...except` block to catch potential errors during ping execution and provide more informative error messages.

* **Parameter Validation:**  It checks if the `url` parameter is provided and returns a 400 Bad Request error if it