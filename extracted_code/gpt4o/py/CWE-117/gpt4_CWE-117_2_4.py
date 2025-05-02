from flask import request, current_app, Flask
import logging

logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)

@app.route('/logger/input', methods=['POST'])
def log_input():
    '''
    Get input data from the request and log it as an error
    '''
    user_input = request.get_json()  # Assuming the input is sent as JSON
    if not user_input:
        return {"error": "No input data provided"}, 400

    current_app.logger.error(f"User input logged as error: {user_input}")
    return {"message": "Input logged successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)
