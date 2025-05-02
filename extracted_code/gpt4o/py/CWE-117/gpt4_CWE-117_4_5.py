from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/get-username")
def logUserName():
    '''
    Get the 'name' from the request
    Log an info message with the user name
    '''
    name = request.args.get('name')  # Extract 'name' parameter from the request
    if name:
        logging.info(f"User name received: {name}")
        return f"Hello, {name}!"
    else:
        logging.info("No user name provided in the request.")
        return "Please provide a 'name' parameter in the query string."

if __name__ == "__main__":
    app.run(debug=True)
