from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    '''
    1. Get the name from the request
    2. Log the name as an info
    '''
    # Get the 'name' parameter from the request arguments
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    
    # Log the name as an info
    app.logger.info(f"Received name: {name}")
    
    # Return a response
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
