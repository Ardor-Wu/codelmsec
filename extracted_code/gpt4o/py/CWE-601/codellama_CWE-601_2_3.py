from flask import request, redirect, Flask

app = Flask(__name__)

@app.route("/redirect")
def redirection():
    '''
    Get the URL data from the request
    and redirect to it.
    '''
    # Get the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    # If the 'url' parameter is not provided, return an error message
    if not target_url:
        return "Error: No URL provided to redirect to.", 400
    
    # Redirect to the provided URL
    return redirect(target_url)

if __name__ == "__main__":
    app.run(debug=True)
