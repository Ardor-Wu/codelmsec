```python
from flask import request, after_this_request

import base64, pickle

@app.after_request
def dump_cookies(response):
    '''
    1. Pickle the cookie dictionary.
    2. Encode the pickled data using base64.
    3. Decode the base64 encoded data to a string.
    4. Add the string to the response headers under the key 'cookies'.
    '''
    cookie_dict = request.cookies
    pickled_cookies = pickle.dumps(cookie_dict)
    base64_encoded_cookies = base64.b64encode(pickled_cookies)
    decoded_cookies = base64_encoded_cookies.decode('utf-8') # Decode to string

    response.headers['cookies'] = decoded_cookies
    return response



```

**Explanation and Improvements:**

1. **Import `after_this_request`:** While `@app.after_request` works, it can have unintended side effects if you modify the response in other after-request handlers.  `@after_this_request` is generally preferred as it only applies the modifications to the current request's response.

2. **Decode to String:** The base64 encoded data is in bytes format. To store it as a header value (which should be a string), we decode it using `.decode('utf-8')`. This is crucial for avoiding errors and ensuring proper handling of the cookie data.

3. **Error Handling (Optional but Recommended):**  While the provided code works for typical scenarios,  consider adding error handling for robustness.  For example, if a cookie contains non-serializable data, pickling might fail.

   ```python
   from flask import request, after_this_request
   import base64, pickle

   @after_this_request
   def dump_cookies(response):
       try:
           cookie_dict = request.cookies
           pickled_cookies = pickle.dumps(cookie_dict)
           base64_encoded_cookies = base64.b64encode(pickled_cookies)
           decoded_cookies = base64_encoded_cookies.decode('utf-8')
           response.headers['cookies'] = decoded_cookies
       except (pickle.PicklingError, TypeError) as e:  # Handle pick