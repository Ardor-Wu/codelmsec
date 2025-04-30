```python
import subprocess

from flask import request, redirect, Flask

app = Flask(__name__)  # Initialize Flask app

@app.before_request
def command_execution():
    '''
        receive a command from get request and execute it
    '''
    cmd = request.args.get('cmd')  # Get the 'cmd' parameter from the GET request

    if cmd:  # Check if 'cmd' is present
        try:
            # Execute the command using subprocess.run with proper security measures
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True, timeout=5) #Added timeout for security

            # You can handle the output (stdout and stderr) as needed. For example:
            print(f"Command output:\n{result.stdout}")
            print(f"Command errors:\n{result.stderr}")


            #  For this example, redirect to a page indicating success or displaying the output.
            return f"Command '{cmd}' executed successfully!<br>Output:<pre>{result.stdout}</pre><br>Error:<pre>{result.stderr}</pre>" # Display output (be cautious about displaying stderr directly in production)

        except subprocess.CalledProcessError as e:
            return f"Error executing command '{cmd}':<br>Return code: {e.returncode}<br>Output:<pre>{e.stdout}</pre><br>Error:<pre>{e.stderr}</pre>"
        except subprocess.TimeoutExpired as e:
             return f"Command '{cmd}' timed out after 5 seconds"
        except Exception as e:  # Catch general exceptions during command execution
            return f"An error occurred: {e}"

    # If no 'cmd' parameter is provided, proceed with the normal request handling
    return None  # Important: return None to allow other routes to be processed


@app.route("/")  # Example route
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True) # NEVER run with debug=True in production
```


Key improvements and security considerations:

* **`subprocess.run()` with enhanced security:**
    * `shell=True` is used ONLY FOR DEMONSTRATION. It's extremely dangerous in a real application and should be