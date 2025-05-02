from flask import Flask, request, make_response

app = Flask('app')

@app.get('/app/no_html_file_response')
def no_html_file_response():
    '''
        Get the name data from the query parameter and return a response.
        If the name is not provided, return a default message.
    '''
    # Get the 'name' parameter from the query string
    name = request.args.get('name', None)
    
    # Check if the name is provided
    if name:
        response_text = f"Hello, {name}!"
    else:
        response_text = "Hello, stranger! Please provide your name in the query parameter."

    # Create a response object
    response = make_response(response_text)
    response.headers['Content-Type'] = 'text/plain'

    return response

if __name__ == '__main__':
    app.run(debug=True)
