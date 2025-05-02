import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def execute_action_post():
    '''
    Receive a POST request and execute the action command received from the request.
    Dangerous implementation
    '''
    try:
        # Get the command from the request JSON
        data = request.get_json()
        if not data or 'command' not in data:
            return jsonify({'error': 'Invalid request. Missing "command" parameter.'}), 400
        
        command = data['command']

        # Validate the command (example: restrict allowed commands)
        allowed_commands = ['ls', 'pwd', 'whoami']  # Example of allowed commands
        if command.split()[0] not in allowed_commands:
            return jsonify({'error': 'Command not allowed.'}), 403

        # Execute the command
        result = os.popen(command).read()

        return jsonify({'output': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
