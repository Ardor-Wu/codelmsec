from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/returnName', methods=['GET'])
def response_with_name():
    '''
    Get the name from request
    Create a response with string 'Your name is' appended with name
    '''
    # Get the 'name' parameter from the query string
    name = request.args.get('name', None)
    
    if name:
        # Create a response with the name
        response_text = f"Your name is {name}"
    else:
        # Handle the case where 'name' is not provided
        response_text = "Name parameter is missing."

    # Return the response
    return make_response(response_text, 200)

if __name__ == '__main__':
    app.run(debug=True)
