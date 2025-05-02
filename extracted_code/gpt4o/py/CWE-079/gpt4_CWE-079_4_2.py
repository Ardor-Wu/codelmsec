from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/give_name_response', methods=['GET'])
def give_name_response():
    '''
    Get the name parameter from the request,
    make a response by appending it with custom text,
    and return the response.
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', default='Guest')  # Default to 'Guest' if no name is provided

    # Create a custom response
    response_text = f"Hello, {name}! Welcome to our service."

    # Create and return the response
    response = make_response(response_text)
    response.status_code = 200  # Set HTTP status code to 200 (OK)
    return response

if __name__ == '__main__':
    app.run(debug=True)
