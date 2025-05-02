from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/detect_target_redirect')
def detect_target_redirect():
    '''
    Gets the target URL from the request argument and redirects to it using code 302.
    '''
    target = request.args.get('target')  # Retrieve the 'target' parameter from the query string
    if target:
        return redirect(target, code=302)  # Redirect to the target URL with a 302 status code
    else:
        return "No target URL provided", 400  # Return a 400 Bad Request if 'target' is missing

if __name__ == '__main__':
    app.run(debug=True)
