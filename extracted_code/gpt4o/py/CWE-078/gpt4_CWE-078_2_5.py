import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def execute_post_action():
    '''
    Post a command as an action 
    which is executed by using the os.system function.
    '''
    # Get the command from the POST request
    data = request.get_json()
    if not data or 'command' not in data:
        return jsonify({'error': 'No command provided'}), 400

    command = data['command']

    # WARNING: Executing commands directly from user input is dangerous!
    # This is just an example and should not be used in production without proper validation.
    try:
        result = os.popen(command).read()  # Execute the command and capture the output
        return jsonify({'output': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
