the base64-encoded value, and returns the decoded name.
    If the decoding fails or 'first_name' is not provided, it returns an error message.
    '''
    try:
        # Extract 'first_name' from the posted JSON data
        data = request.get_json()
        if not data or 'first_name' not in data:
            return {"error": "Missing 'first_name' in request data"}, 400

        # Decode the base64-encoded 'first_name'
        encoded_name = data['first_name']
        decoded_name = base64.b64decode(encoded_name).decode('utf-8')

        # Return the decoded name
        return {"decoded_name": decoded_name}, 200

    except (base64.binascii.Error, UnicodeDecodeError):
        # Handle decoding errors
        return {"error": "Invalid base64-encoded 'first_name'"}, 400


if __name__ == '__main__':
    app.run(debug=True)