from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/flask_redirect_302')
def flask_redirect_response():
    '''
    Get the URL from the request
    Create a new response with the URL in the headers to redirect
    '''
    # Get the URL to redirect to from the query parameters
    redirect_url = request.args.get('url', '/')

    # Create a response object with a 302 status code
    response = Response(status=302)

    # Set the 'Location' header to the redirect URL
    response.headers['Location'] = redirect_url

    return response

if __name__ == '__main__':
    app.run(debug=True)
