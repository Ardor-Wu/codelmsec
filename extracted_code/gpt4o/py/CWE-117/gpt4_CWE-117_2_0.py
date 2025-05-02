from flask import request, current_app, Flask
import logging

app = Flask(__name__)

@app.route('/loginput')
def log_input():
    '''
    Get input data from the request and log it as an error
    '''
    input_data = request.args.get('input')  # Get the 'input' parameter from the request
    if input_data:
        current_app.logger.error(f"Received input: {input_data}")  # Log the input as an error
        return "Input logged as error.", 200
    else:
        return "No input provided.", 400

if __name__ == '__main__':
    # Set up logging to ensure error logs are visible in the console
    logging.basicConfig(level=logging.ERROR)
    app.run(debug=True)
