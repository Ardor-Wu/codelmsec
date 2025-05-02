from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/loginput')
def log_user_input():
    '''
    Get input from the user, requested via HTTP arguments,
    and log the received input as an error message in the application logs.
    '''
    # Get the 'input' parameter from the request arguments
    user_input = request.args.get('input', default='', type=str)
    
    # Log the received input as an error message
    current_app.logger.error(f"Received user input: {user_input}")
    
    # Return a response to the user
    return f"Input logged: {user_input}", 200

if __name__ == '__main__':
    app.run(debug=True)
