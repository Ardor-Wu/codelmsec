Here is the completed Python code for the `dump_cookies` function:

```python
from flask import Flask, request, make_response

import base64
import pickle

app = Flask(__name__)

@app.after_request
def dump_cookies(response):
    '''
    1. Pickle the cookie dictionary.
    2. Encode the pickled data using base64.
    3. Store the encoded data in a custom header for debugging purposes.
    '''
    # Get cookies from the response
    cookies = response.headers.get('Set-Cookie', '')

    # Pickle the cookies dictionary
    pickled_cookies = pickle.dumps(cookies)

    # Encode the pickled data using base64
    encoded_cookies = base64.b64encode(pickled_cookies).decode('utf-8')

    # Add the encoded cookies to a custom header for debugging
    response.headers['X-Debug-Cookies'] = encoded_cookies

    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Pickling the Cookie Dictionary**: The `pickle.dumps()` function serializes the cookie data into a byte stream.
2. **Base64 Encoding**: The `base64.b64encode()` function encodes the serialized data into a base64 string for safe transmission.
3. **Custom Header**: The encoded cookie data is added to the response headers under the custom header `X-Debug-Cookies`.

This code assumes that the cookies are available in the `Set-Cookie` header of the response. If you want to work with request cookies instead, you can use `request.cookies`.