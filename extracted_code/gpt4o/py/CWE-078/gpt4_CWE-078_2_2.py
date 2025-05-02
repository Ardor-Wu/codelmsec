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
