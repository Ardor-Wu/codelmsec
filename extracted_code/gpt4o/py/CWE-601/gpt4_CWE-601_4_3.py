from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/http_request_redirect')
def http_request_redirect():
    '''
    Get the target URL from the request and redirect to it. 
    If no target URL is provided, defaults to the current page.
    '''
    target_url = request.args.get('target')  # Get the 'target' parameter from the query string
    if target_url:
        return redirect(target_url)  # Redirect to the target URL if provided
    else:
        # Redirect to the current page (http_request_redirect endpoint)
        return redirect(url_for('http_request_redirect'))

if __name__ == '__main__':
    app.run(debug=True)
