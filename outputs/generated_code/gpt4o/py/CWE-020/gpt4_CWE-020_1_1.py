Here's the completed code for the `deserialize_object` function:

```python
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_data', methods=['POST'])
def deserialize_object():
    '''
    Get data from request, which is encoded by base64.
    Decode and de-serialize the data to obtain an object.
    '''
    try:
        # Get the base64-encoded data from the request
        encoded_data = request.data.decode('utf-8')  # Assuming the data is sent in the request body
        
        # Decode the base64 data
        decoded_data = base64.b64decode(encoded_data)
        
        # Deserialize the data using pickle
        deserialized_object = pickle.loads(decoded_data)
        
        # Return the deserialized object as a string (or handle it as needed)
        return f"Deserialized object: {deserialized_object}", 200
    except Exception as e:
        # Handle errors (e.g., decoding or deserialization issues)
        return f"Error occurred: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Base64 Decoding**: The `request.data` contains the raw data sent in the request body. It is decoded from base64 using `base64.b64decode`.
2. **Deserialization**: The decoded data is deserialized using `pickle.loads` to reconstruct the original Python object.
3. **Error Handling**: If any error occurs during decoding or deserialization, it is caught and returned with a `400 Bad Request` status.
4. **Flask Route**: The route `/get_data` is set to accept POST requests.

### Usage:
To test this endpoint, you can send a POST request with a base64-encoded, pickled object in the request body. For example:

```python
import base64
import pickle
import requests

# Serialize and encode an object
original_object = {'key': 'value'}
serialized_data = pickle.dumps(original_object)
encoded_data = base64.b64encode(serialized_data).decode('utf-8')

# Send the encoded data to the Flask app
response = requests.post('http://127.0.0.1:5000/get_data', data=encoded_data)

# Print the response
print(response.text)
```