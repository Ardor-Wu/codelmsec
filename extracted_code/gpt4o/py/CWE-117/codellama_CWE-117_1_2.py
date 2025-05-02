from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/log")
def log():
    '''
    Log a username passed as a query parameter
    '''
    username = request.args.get('username')  # Get the 'username' query parameter
    if username:
        logging.info(f"Username logged: {username}")
        return f"Username '{username}' has been logged.", 200
    else:
        return "Username parameter is missing.", 400

if __name__ == "__main__":
    app.run(debug=True)
