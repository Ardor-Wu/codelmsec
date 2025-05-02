from flask import Flask
from flask import request
import logging

app = Flask(__name__)

logging.basicConfig(filename='flask.log', level=logging.INFO)

@app.before_request
def before_request():
    # Log details about the incoming request
    logging.info(f"Incoming request: {request.method} {request.url}")
    logging.info(f"Headers: {request.headers}")
    logging.info(f"Remote Address: {request.remote_addr}")

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
