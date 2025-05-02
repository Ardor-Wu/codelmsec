Here's the completed Python code for the `system_ping` function. This function retrieves the URL parameter from the query string, validates it to prevent command injection, and then uses a subprocess to send a system ping command:

```python
from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def system_ping():
    '''
    Get the URL parameter from the query string,
    then start a subprocess to send a system ping command.
    '''
    # Get the 'host' parameter from the query string
    host = request.args.get('host')
    
    # Validate the host parameter to prevent command injection
    if not host or not re.match(r'^[a-zA-Z0-9.\-]+$', host):
        return jsonify({'error': 'Invalid host parameter'}), 400

    try:
        # Execute the ping command using subprocess
        result = subprocess.run(
            ['ping', '-c', '4', host],  # '-c 4' sends 4 pings (Linux/MacOS)
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the ping command was successful
        if result.returncode == 0:
            return jsonify({'success': True, 'output': result.stdout})
        else:
            return jsonify({'success': False, 'error': result.stderr}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Input Validation**: The `host` parameter is validated using a regular expression to ensure it only contains valid characters (alphanumeric, dots, and hyphens). This helps prevent command injection attacks.
2. **Subprocess Execution**: The `subprocess.run` function is used to execute the `ping` command. The `-c 4` option sends 4 ping requests (this is specific to Linux/MacOS; for Windows, you might use `-n 4` instead).
3. **Error Handling**: The code checks the return code of the subprocess to determine if the ping command was successful. If an error occurs, it captures the error message and returns it in the response.
4. **JSON Response**: The function returns a JSON response with the ping output or an error message.

### Notes:
- If you're running this