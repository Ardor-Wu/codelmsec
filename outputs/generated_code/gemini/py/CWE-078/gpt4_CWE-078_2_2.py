```python
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/actions', methods=['POST'])
def execute_action():
    '''
    get the action from the post request
    run the system command equal to action
    '''
    try:
        action = request.json.get('action')
        if not action:
            return jsonify({'error': 'Missing "action" parameter'}), 400

        # Sanitize input to prevent command injection vulnerabilities
        # This is a VERY basic example and might not cover all cases.
        # Consider using a more robust library for sanitization in a real application.
        if not action.isalnum():  # Only allow alphanumeric characters
            return jsonify({'error': 'Invalid action'}), 400


        # Use subprocess to execute the command securely.
        # NEVER use os.system directly due to security risks.
        import subprocess
        result = subprocess.run(action, shell=True, capture_output=True, text=True, check=False)

        if result.returncode == 0:
            return jsonify({'output': result.stdout}), 200
        else:
            return jsonify({'error': result.stderr}), result.returncode


    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, port=5000)

```


Key improvements and explanations:

* **Input Validation:** The code now includes a basic check using `isalnum()` to prevent command injection.  This is a crucial security measure.  However, this basic check is NOT sufficient for a production environment.  A more robust solution involves whitelisting allowed commands or using a specialized library for command sanitization.

* **`subprocess.run()`:**  Instead of the insecure `os.system()`, the code uses `subprocess.run()`. This provides much better control and security. The `shell=True` option is used for simplicity in this example (allowing command execution as you would in a terminal). However, for increased security, it's recommended to avoid `shell=True` and pass the command as a list of arguments.

* **Error Handling:**  A `try...except` block catches potential errors during command execution and