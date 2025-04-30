```python
import os
import subprocess
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

# Extremely dangerous!  Only for demonstration purposes in a controlled environment.
# NEVER use this in a production setting.
def command_execution(request):
    """
    Receives a command from a POST request and executes it.
    """
    if request.method != 'POST':
        return jsonify({'error': 'Only POST requests are allowed'}), 405

    try:
        # Get the command from the request body (JSON format is recommended)
        data = request.get_json()
        if not data or 'command' not in data:
            return jsonify({'error': 'Missing "command" in request body'}), 400

        command = data['command']

        # Sanitize input (CRITICAL but insufficient - see below)
        # This is a VERY basic example and easily bypassed.  Do NOT rely on this.
        if ';' in command or '|' in command or '&' in command:  # Basic attempt to prevent command injection
            return jsonify({'error': 'Invalid characters in command'}), 400