from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/log", methods=["GET"])
def log():
    '''
    Get the input from the user and log it at the info level
    '''
    user_input = request.args.get("message")  # Get the 'message' parameter from the query string
    if user_input:
        logging.info(f"User input: {user_input}")  # Log the input at the INFO level
        return f"Logged: {user_input}", 200
    else:
        return "No message provided", 400

if __name__ == "__main__":
    app.run(debug=True)
