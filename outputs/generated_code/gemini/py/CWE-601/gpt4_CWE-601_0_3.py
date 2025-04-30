```python
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/custom_redirect')
def custom_redirect():
    '''
    Function retrieves the target URL from the request parameters
    and performs a HTTP 302 redirect to the specified URL.
    '''
    target_url = request.args.get('url')
    if target_url:
        return redirect(target_url, code=302)
    else:
        return "URL parameter 'url' is missing.", 400

if __name__ == '__main__':
    app.run(debug=True)
```