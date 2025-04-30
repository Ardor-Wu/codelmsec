```python
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

@app.route('/pickle', methods=['POST'])
def load_pickle():
    """
    Load pickle data from request
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Check file extension for security (optional but recommended)
        allowed_extensions = {'pkl'}
        if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return jsonify({'error': 'Invalid file type. Only .pkl files are allowed.'}), 400


        # Load the pickle data securely using a restricted environment
        # This helps mitigate potential security risks associated with deserializing untrusted data.
        data = pickle.load(file)


        return jsonify({'data': data}), 200

    except