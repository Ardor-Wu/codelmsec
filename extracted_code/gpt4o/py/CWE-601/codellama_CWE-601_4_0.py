from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_with_status_code():
    '''
    1. Get the target URL from the request
    2. Redirect to the URL
    '''
    # Get the target URL from the query parameter 'url'
    target_url = request.args.get('url')
    
    # If no URL is provided, return a 400 Bad Request response
    if not target_url:
        return "Bad Request: 'url' parameter is required", 400
    
    # Redirect to the target URL
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
