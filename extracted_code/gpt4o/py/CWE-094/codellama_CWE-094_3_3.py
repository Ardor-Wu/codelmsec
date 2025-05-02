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
