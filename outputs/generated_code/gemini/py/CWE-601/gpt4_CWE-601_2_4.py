```python
from flask import request, redirect, Flask
app = Flask(__name__)

@app.route('/redirect_to_next')
def redirect_to_next():
    '''
    get url data from the request and redirect to the given url
    '''
    url = request.args.get("next", None)
    if url:
        return redirect(url)
    else:
        return "No 'next' parameter provided", 400
```