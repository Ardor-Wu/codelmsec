from flask import Flask
from flask import request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/log_name')
def logUserName():
    '''
    Get the 'name' from the request and log it as an info
    '''
    name = request.args.get('name')
    if name:
        logging.info(f"Received name: {name}")
        return f"Name '{name}' logged successfully!", 200
    else:
        return "No name provided in the request.", 400

if __name__ == '__main__':
    app.run(debug=True)
