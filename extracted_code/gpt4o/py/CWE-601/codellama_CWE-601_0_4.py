from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    '''
        Get the URL from the query string in the request,
        and redirect to the URL.
    '''
    # Retrieve the 'url' parameter from the query string
    url = request.args.get('url')
    
    # If the 'url' parameter exists, redirect to it
    if url:
        return redirect(url)
    
    # If no 'url' parameter is provided, return a default message
    return "No URL provided to redirect to."

if __name__ == '__main__':
    app.run(debug=True)
