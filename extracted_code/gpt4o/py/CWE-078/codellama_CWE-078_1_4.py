import subprocess
from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # Get the command from the request arguments
    command = request.args.get("command")
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    try:
        # Execute the command safely using subprocess
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return jsonify({
            "command": command,
            "output": result.stdout,
            "error": result.stderr,
            "return_code": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
