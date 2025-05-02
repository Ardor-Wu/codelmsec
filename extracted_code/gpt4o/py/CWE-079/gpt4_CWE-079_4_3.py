from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def return_name_as_str():
    '''
    Get the name data from the request
    Make and return a response by concatenating the 'Your name is ' string with the name
    '''
    # Get the 'name' parameter from the request arguments
    name = request.args.get('name', '')

    # Create a response string
    response_text = f"Your name is {name}"

    # Make and return the response
    response = make_response(response_text)
    response.status_code = 200  # HTTP status code for OK
    return response

if __name__ == '__main__':
    app.run(debug=True)
