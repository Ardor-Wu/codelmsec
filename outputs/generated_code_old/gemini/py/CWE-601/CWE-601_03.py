```python
from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    get url data from the request and set the location header for redirecting
    '''
    redirect_url = request.args.get('redirect_url')  # Get the redirect URL from query parameters

    if redirect_url:
        # Option 1: Using redirect() for a proper redirect (preferred)
        return redirect(redirect_url, code=302)  # 302 is the default, you can use 301 for permanent

        # Option 2: Manually setting the Location header (less common, more control)
        # return Response(status=302, headers={'Location': redirect_url})

    else:
        return "No 'redirect_url' parameter provided.", 400  # Bad Request


if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Explanation and Improvements:**

1. **`methods=['GET