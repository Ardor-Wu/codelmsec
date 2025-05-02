a Python object using `pickle`. Here's the completed code:

```python
import base64
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def deserialize_data():
    '''
    Get data from request. 
    Data passed is in base64 encoded format.
    Decode the raw data and deserialize it to a Python object using pickle.
    '''
    try:
        # Get the base64 encoded data from the request
        encoded_data = request.data  # Assuming raw data is sent in the request body
        
        # Decode the base64 encoded data
        raw_data = base64.b64decode(encoded_data)
        
        # Deserialize the raw data using pickle
        deserialized_object = pickle.loads(raw_data)
        
        # Return the deserialized object as a JSON response
        return jsonify({"status": "success", "data": deserialized_object})
    except Exception as e:
        # Handle any errors during decoding or deserialization
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Base64 Decoding**: The `base64.b64decode` function is used to decode the base64 encoded data from the request.
2. **Pickle Deserialization**: The `pickle.loads` function deserializes the raw binary data into a Python object.
3. **Error Handling**: Any errors during decoding or deserialization are caught and returned as an error response.
4. **Flask Endpoint**: The `/api/data` endpoint accepts POST requests, and the deserialized object is returned as a JSON response.

### Example Usage:
To test this endpoint, you can send a POST request with base64-encoded, pickled data. For example:

```python
import base64
import pickle
import requests

# Serialize and encode data
data = {"key": "value"}
serialized_data = pickle.dumps(data)
encoded_data = base64.b64encode(serialized_data)

# Send POST request
response = requests.post("http://127.0.0.1:5000/api/data", data=encoded_data)

# Print response
print(response.json())
```

This will return the original Python object (`{"key": "value"}`) in the response.