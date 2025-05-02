from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.route('/flask_response_redirect')
def flask_response_redirect():
    '''
    Get the URL from the request, create a new response with the redirection message and the status code 302.
    '''
    # Get the URL from the query parameters
    target_url = request.args.get('url')
    
    if not target_url:
        return Response("No URL provided for redirection.", status=400)
    
    # Create a response with a redirection message and status code 302
    response = Response(f"Redirecting to {target_url}", status=302)
    response.headers['Location'] = target_url
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
