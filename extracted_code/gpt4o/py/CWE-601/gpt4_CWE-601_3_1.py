from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.route('/flask_http_response')
def flask_http_response():
    '''
    Get the URL from the request and generate an HTTP response with a 302 status code
    for redirecting the server to the specified URL.
    '''
    # Extract the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    if target_url:
        # Redirect to the target URL with a 302 status code
        return redirect(target_url, code=302)
    else:
        # If no URL is provided, return a bad request response
        return Response("Missing 'url' parameter", status=400)

if __name__ == '__main__':
    app.run(debug=True)
