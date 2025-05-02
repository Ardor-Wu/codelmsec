from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/handler')
def handle_redirection():
    '''
    Get target URL from request. The second parameter in the get 
    method provides a default value if 'target'
    doesn't exist in the request arguments. Then, redirect the user to the target URL.
    '''
    target_url = request.args.get('target', 'https://default-url.com')
    return redirect(target_url)

if __name__ == '__main__':
    app.run(debug=True)
