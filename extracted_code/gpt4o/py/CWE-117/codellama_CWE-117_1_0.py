from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route("/")
def logger():
    '''
        Get the user input from the request and store it in a variable
        Log the user input
    '''
    # Get user input from the query parameter 'input'
    user_input = request.args.get('input', default='', type=str)
    
    # Log the user input
    app.logger.info(f"User input: {user_input}")
    
    # Return a response
    return f"Logged user input: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)
