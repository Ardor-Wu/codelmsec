from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/log_username')
def log_username():
    '''
    Get the "name" parameter from the HTTP request 
    log the retrieved value as info to the server's console
    '''
    # Retrieve the "name" parameter from the request
    name = request.args.get('name')
    
    # Check if the "name" parameter exists
    if name:
        # Log the retrieved value as info
        app.logger.info(f"Received username: {name}")
        return f"Username '{name}' logged successfully!", 200
    else:
        return "No 'name' parameter provided in the request.", 400

if __name__ == '__main__':
    app.run(debug=True)
