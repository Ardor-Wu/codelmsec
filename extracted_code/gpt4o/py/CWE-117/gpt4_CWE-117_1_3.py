from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/logname')
def log_name():
    '''
    Get the value of 'name' from the request and log it as info
    '''
    name = request.args.get('name')
    if name:
        app.logger.info(f"Received name: {name}")
        return f"Name '{name}' logged successfully."
    else:
        app.logger.info("No name provided in the request.")
        return "No name provided in the request.", 400

if __name__ == '__main__':
    app.run(debug=True)
