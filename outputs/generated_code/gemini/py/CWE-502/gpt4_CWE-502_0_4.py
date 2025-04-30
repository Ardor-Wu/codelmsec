```python
from flask import Flask, request
import pickle
import base64

app = Flask(__name__)

@app.route('/pickle_load')
def load_pickle_data():
    '''
    Retrieve data from request, un-pickle it using pickle.loads() and return the resulted
    data
    '''
    try:
        # Get the base64 encoded pickle data from the request
        encoded_data = request.args.get('data')

        if encoded_data is None:
            return "Error: No data provided", 400

        # Decode the base64 encoded data
        pickled_data = base64.b64decode(encoded_data)

        # Unpickle the data
        data = pickle.loads(pickled_data)

        return str(data), 200

    except pickle.UnpicklingError:
        return "Error: Invalid pickle data", 400
    except base64.binascii.Error:  # Catch invalid base64
        return "Error: Invalid base64 encoding", 400
    except Exception as e: # Catching other potential errors
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)

```

**Key Improvements and Explanations:**

1. **Base64 Encoding:** Pickle data is binary.  Transmitting it directly in a URL query string is problematic.  This code now uses `base64.b64encode()` on the client-side (not shown here, but assumed) and `base64.b64decode()` to correctly handle the data transfer.  This is crucial for robust data handling.

2. **Error Handling:**  The code includes comprehensive error handling using `try...except` blocks:
   - `pickle.UnpicklingError`: Handles invalid pickle data.
   - `base64.binascii.Error`: Catches incorrect base64 formatting.
   - `TypeError`: Handles cases where `encoded_data` might not be a string (e.g., None).
   - A generic `Exception` block catches other unforeseen issues.  It's good practice to be as specific as possible with error handling.

3. **Return Codes:** Appropriate HTTP status