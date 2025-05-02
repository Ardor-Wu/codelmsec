from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/get_and_respond_name', methods=['GET'])
def get_and_respond_name():
    '''
    Get the 'name' parameter from request
    Create a response with the value of 'name'
    Return
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', default="Guest")  # Default to "Guest" if 'name' is not provided
    
    # Create a response with the value of 'name'
    response = make_response(f"Hello, {name}!")
    
    # Return the response
    return response

if __name__ == '__main__':
    app.run(debug=True)
