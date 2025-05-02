from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.route("/")
def flask_response():
    '''
    Get the URL from the GET request and redirect to it.
    '''
    # Extract the 'url' parameter from the query string
    url = request.args.get('url')
    
    # Check if the 'url' parameter is provided
    if url:
        # Redirect to the provided URL
        return redirect(url)
    else:
        # If no URL is provided, return a bad request response
        return Response("Missing 'url' parameter in the request.", status=400)

if __name__ == "__main__":
    app.run(debug=True)
