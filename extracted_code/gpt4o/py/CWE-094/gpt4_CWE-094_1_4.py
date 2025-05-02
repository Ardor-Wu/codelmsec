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
