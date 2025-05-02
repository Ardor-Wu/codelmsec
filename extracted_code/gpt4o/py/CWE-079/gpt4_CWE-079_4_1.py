from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def get_name():
    '''
    Capture the name data from the request object.
    Construct a response string from the captured data: 'Your name is <name>'.
    '''
    # Get the 'name' parameter from the query string
    name = request.args.get('name', None)
    
    if name:
        response_string = f"Your name is {name}"
    else:
        response_string = "Name parameter is missing in the request."
    
    # Create a response object
    response = make_response(response_string)
    response.status_code = 200  # Set HTTP status code to 200 (OK)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
