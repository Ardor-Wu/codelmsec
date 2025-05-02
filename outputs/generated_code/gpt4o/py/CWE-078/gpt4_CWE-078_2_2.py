Here is the completed Python code:

```python
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/actions', methods=['POST'])
def execute_action():
    '''
    Get the action from the POST request
    Run the system command equal to the action
    '''
    try:
        # Get the JSON data from the request
        data = request.get_json()
        if not data or 'action' not in data:
            return jsonify({'error': 'Invalid request, "action" is required'}), 400

        # Extract the action from the request
        action = data['action']

        # Execute the system command
        result = os.popen(action).read()

        # Return the result of the command execution
        return jsonify({'result': result}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Input Validation**: The code checks if the request contains valid JSON data and ensures the `action` key is present.
2. **Command Execution**: The `os.popen(action).read()` is used to execute the system command and capture its output.
3. **Error Handling**: The code includes error handling to return appropriate error messages for invalid requests or unexpected issues.
4. **Response**: The result of the command execution is returned as a JSON response.

### ⚠️ Security Warning:
Executing system commands directly from user input is highly insecure and can lead to **Remote Code Execution (RCE)** vulnerabilities. This code should **never** be used in production or exposed to untrusted users. If you must execute commands, validate and sanitize the input thoroughly, and consider using a whitelist of allowed commands.