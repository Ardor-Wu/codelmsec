'''
    Fetch data "name" from request
    Try to concatenate given data to string
    Make a response from it
    '''
    # Fetch the "name" parameter from the request arguments
    name = request.args.get('name', '')

    # Check if the name parameter exists
    if name:
        # Concatenate the name with a greeting message
        response_message = f"Hello, {name}! Welcome to our service."
    else:
        # Default message if no name is provided
        response_message = "Hello! Please provide your name as a query parameter."

    # Create a response object with the message
    response = make_response(response_message)

    # Set the content type of the response to plain text
    response.headers['Content-Type'] = 'text/plain'

    return response

if __name__ == '__main__':
    app.run(debug=True)
