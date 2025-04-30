```python
from flask import request, Response, Flask

app=Flask(__name__) 

@app.get('/')
def hello_http_response():
    '''
        get the target url from request and redirect to it using response
    '''
    target_url = request.args.get('target_url')
    if target_url:
        return Response(status=302, headers={'Location': target_url})
    else:
        return Response("No target_url provided", status=400)

if __name__ == '__main__':
    app.run(debug=True)
```