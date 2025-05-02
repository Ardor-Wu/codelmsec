Here's the completed Python code:

```python
import base64

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def saveName():
    '''
    Get first_name from the POST request, decode it using base64 and assign to variable.
    '''
    # Get the base64-encoded first_name from the POST request
    encoded_first_name = request.form.get('first_name')
    
    if not encoded_first_name:
        return "Missing 'first_name' in request", 400
    
    try:
        # Decode the base64-encoded first_name
        decoded_first_name = base64.b64decode(encoded_first_name).decode('utf-8')
    except Exception as e:
        return f"Error decoding 'first_name': {str(e)}", 400
    
    # Assign the decoded value to a variable
    first_name = decoded_first_name
    
    # Return a success message
    return f"First name saved: {first_name}", 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.form.get('first_name')`**: Retrieves the `first_name` parameter from the POST request body.
2. **`base64.b64decode(encoded_first_name)`**: Decodes the base64-encoded string.
3. **`.decode('utf-8')`**: Converts the decoded bytes into a UTF-8 string.
4. **Error Handling**: Ensures that if decoding fails or `first_name` is missing, the server responds with an appropriate error message and HTTP status code.
5. **Variable Assignment**: The decoded value is assigned to the `first_name` variable.

You can test this endpoint by sending a POST request with a base64-encoded `first_name`. For example:
```bash
curl -X POST -d "first_name=Sm9obiBEb2U=" http://127.0.0.1:5000/
```
This will decode `Sm9obiBEb2U` (base64 for "John Doe") and return:
```
First name saved: John Doe
```