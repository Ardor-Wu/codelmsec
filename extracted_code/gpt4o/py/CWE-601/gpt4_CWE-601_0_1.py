from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/flask_custom_redirect')
def flask_custom_redirect():
    '''
    Get target URL from the request and redirect to it with HTTP status code 302
    '''
    target = request.args.get('target')  # Extract the 'target' parameter from the query string
    if target:
        return redirect(target, code=302)  # Redirect to the target URL with HTTP status code 302
    else:
        return "Target URL not provided", 400  # Return a 400 Bad Request if no target URL is provided

if __name__ == '__main__':
    app.run(debug=True)
