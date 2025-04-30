```python
from flask import request, Response, Flask
app = Flask(__name__)

@app.route('/flask_redirect_302')
def flask_redirect_response():
    '''
    get the url from the request
    create a new response with the url in the headers to redirect
    '''
    url = request.args.get('url')
    if url:
        return Response(status=302, headers={'Location': url})
    else:
        return Response("No 'url' parameter provided", status=400)

if __name__ == '__main__':
    app.run(debug=True)
```