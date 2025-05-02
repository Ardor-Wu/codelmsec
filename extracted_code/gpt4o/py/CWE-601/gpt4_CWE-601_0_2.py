from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/flask_redirect_with_code")
def flask_redirect_with_code():
    '''
    Extract the 'target' parameter from GET request, if it doesn't exist use empty string 
    as the default value. Redirect to the target URL with a 302 status code.
    '''
    target = request.args.get('target', '')  # Extract 'target' parameter, default to empty string
    if target:
        return redirect(target, code=302)  # Redirect to the target URL with a 302 status code
    else:
        return "No target URL provided", 400  # Return a 400 Bad Request if 'target' is missing

if __name__ == "__main__":
    app.run(debug=True)
