'''
    Listen POST request and extract 'action' from the request parameters.
    The 'action' parameter will determine which system command to execute.
    '''
    # Extract the 'action' parameter from the request
    action = request.form.get('action')

    if not action:
        return {"error": "No action provided"}, 400

    # Define a whitelist of allowed actions to prevent arbitrary command execution
    allowed_actions = {
        "list_files": "ls",
        "current_directory": "pwd",
        "disk_usage": "df -h"
    }

    # Check if the action is in the whitelist
    if action not in allowed_actions:
        return {"error": "Invalid action"}, 400

    # Execute the corresponding system command
    command = allowed_actions[action]
    try:
        result = os.popen(command).read()
        return {"action": action, "result": result}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)
