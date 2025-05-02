import base64
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/decode')
def decode_object():
    '''
    Get data from request args
    Encode the data with 'utf-8'
    Decode the received data as bytes by using base64
    Deserialize the decoded bytes
    '''
    # Get the base64-encoded data from the request arguments
    encoded_data = request.args.get('data')
    if not encoded_data:
        return jsonify({"error": "Missing 'data' parameter"}), 400

    try:
        # Decode the base64-encoded string into bytes
        decoded_bytes = base64.b64decode(encoded_data.encode('utf-8'))
        
        # Deserialize the decoded bytes into a Python object
        deserialized_object = pickle.loads(decoded_bytes)
        
        # Return the deserialized object as a JSON response
        return jsonify({"decoded_object": deserialized_object})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
