looks for the 'action' key in the JSON payload of the request. Based on the value of 'action', it performs a specific task and returns an appropriate response. If the 'action' key is missing or the value is invalid, it returns an error message.

Here is the completed code:

```python
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_action', methods=['POST'])
def execute_post_action():
    '''
    On receiving a POST request, get the value for 'action'. It
    looks for the 'action' key in the JSON payload of the request.
    Based on the value of 'action', it performs a specific task and
    returns an appropriate response. If the 'action' key is missing
    or the value is invalid, it returns an error message.
    '''
    # Ensure the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400

    # Parse the JSON payload
    data = request.get_json()

    # Check if 'action' key exists in the payload
    if 'action' not in data:
        return jsonify({"error": "'action' key is missing in the request"}), 400

    # Get the value of 'action'
    action = data['action']

    # Perform actions based on the value of 'action'
    if action == 'say_hello':
        return jsonify({"message": "Hello, world!"}), 200
    elif action == 'get_working_directory':
        cwd = os.getcwd()
        return jsonify({"working_directory": cwd}), 200
    elif action == 'list_files':
        files = os.listdir('.')
        return jsonify({"files": files}), 200
    else:
        return jsonify({"error": f"Invalid action: {action}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Request Validation**: The code checks if the incoming request contains JSON data using `request.is_json`. If not, it returns an error response with a 400 status code.
2. **Action Key Check**: It ensures the JSON payload contains the `action` key. If missing, it returns an error response.
3. **Action Handling**: Based on the value of the `action` key:
   - `say_hello`: Returns a simple greeting message.
  