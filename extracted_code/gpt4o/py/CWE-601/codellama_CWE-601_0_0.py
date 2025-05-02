from flask import Flask, request, redirect

app = Flask('my_app')

@app.route('/redirector')
def http_redirect():
    target = request.args.get('target')  # Retrieve the 'target' query parameter
    if not target:
        return "Missing 'target' parameter", 400  # Return a 400 Bad Request if 'target' is not provided
    return redirect(location=target, code=302)  # Redirect to the target URL

if __name__ == '__main__':
    app.run(debug=True)
