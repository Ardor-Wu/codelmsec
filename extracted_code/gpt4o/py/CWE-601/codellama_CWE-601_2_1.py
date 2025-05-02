from flask import request, redirect, Flask

app = Flask(__name__)

@app.route("/redirect_url")
def redirect_url():
    '''
    Get URL data from the request and redirect to that URL.
    '''
    # Extract the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    # Check if the URL parameter exists
    if target_url:
        # Redirect to the specified URL
        return redirect(target_url)
    else:
        # Return an error message if no URL is provided
        return "Error: No URL provided to redirect to.", 400

if __name__ == "__main__":
    app.run(debug=True)
