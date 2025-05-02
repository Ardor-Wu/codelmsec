from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirection():
    '''
    Get the URL from the request and return a response with redirection to the specified URL.
    '''
    url = request.args.get("url")  # Get the 'url' parameter from the request arguments
    if url:
        return redirect(url)  # Redirect to the specified URL
    else:
        return Response("No URL provided", status=400)  # Return a 400 Bad Request if no URL is provided

if __name__ == "__main__":
    app.run(debug=True)
