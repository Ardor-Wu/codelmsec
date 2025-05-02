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
