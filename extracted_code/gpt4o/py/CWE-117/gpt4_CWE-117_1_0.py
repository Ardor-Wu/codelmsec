from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

@app.route('/log')
def log_user_name():
    '''
    Get the user name from the request and log it as an information (user's name)
    '''
    name = request.args.get('name')  # Retrieve the 'name' parameter from the request
    if name:
        logging.info(f"User's name: {name}")  # Log the user's name as information
        return f"Logged user's name: {name}", 200
    else:
        return "Name parameter is missing.", 400

if __name__ == '__main__':
    app.run(debug=True)
