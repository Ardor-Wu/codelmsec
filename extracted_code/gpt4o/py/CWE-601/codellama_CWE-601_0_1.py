from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_target():
    '''
    Get the target URL from the request and redirect to it with the HTTP code 302.
    '''
    target_url = request.args.get('target')  # Get the 'target' parameter from the query string
    if target_url:
        return redirect(target_url, code=302)  # Redirect to the target URL with HTTP status code 302
    else:
        return "Target URL not provided", 400  # Return a 400 Bad Request if no target URL is provided

if __name__ == '__main__':
    app.run(debug=True)
