Here's the completed Python code for the `redirect_it` function. This function decodes the request data using Base64, then deserializes it using `pickle`:

```python
@app.route("/app")
def redirect_it():
    '''
    Decode the request data, then deserialize it
    '''
    # Get the encoded data from the request
    encoded_data = request.args.get('data')
    
    if not encoded_data:
        return "No data provided", 400
    
    try:
        # Decode the Base64-encoded data
        decoded_data = base64.b64decode(encoded_data)
        
        # Deserialize the data using pickle
        deserialized_data = pickle.loads(decoded_data)
        
        # Return the deserialized data as a response
        return f"Deserialized Data: {deserialized_data}", 200
    except Exception as e:
        return f"Error processing data: {str(e)}", 400
```

### Explanation:
1. **Request Data**: The function retrieves the `data` parameter from the query string (`request.args.get('data')`).
2. **Base64 Decoding**: The `base64.b64decode` function is used to decode the Base64-encoded string.
3. **Deserialization**: The `pickle.loads` function deserializes the decoded data back into its original Python object.
4. **Error Handling**: If any error occurs during decoding or deserialization, the function returns an error message with a `400 Bad Request` status code.

### Example Usage:
If you send a request to `/app` with a Base64-encoded and pickled object in the `data` parameter, the endpoint will decode and deserialize it.

**Note**: Be cautious when using `pickle` for deserialization, especially with untrusted input, as it can lead to security vulnerabilities (e.g., arbitrary code execution). If this is for production use, consider safer alternatives like JSON or custom serialization methods.