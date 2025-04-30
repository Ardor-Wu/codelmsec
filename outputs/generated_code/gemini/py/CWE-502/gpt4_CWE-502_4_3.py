```python
from flask import request, Flask, jsonify
import pickle
import base64
import os

app = Flask(__name__)

@app.route('/unpickle')
def unpickle_data():
    '''
    get data from request, Unpickle it , and return
    '''
    try:
        data_str = request.args.get('data')
        if not data_str:
            return jsonify({'error': 'Data parameter is missing'}), 400

        # Data should be base64 encoded to handle potential binary data and URL encoding issues
        try:
            data_bytes = base64.b64decode(data_str)
        except Exception as e:
            return jsonify({'error': 'Invalid base64 encoding'}), 400


        try:
            # Use a restricted environment for unpickling for security
            unpickled_data = restrict_unpickle(data_bytes)
        except pickle.UnpicklingError as e:
            return jsonify({'error': 'Invalid pickle data'}), 400
        except RestrictedUnpicklingError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:  # Catch other potential errors during unpickling
            return jsonify({'error': 'An error occurred during unpickling'}), 500


        return jsonify(unpickled_data), 200

    except Exception as e: # Catch any unexpected errors
        return jsonify({'error': 'An unexpected error occurred'}), 500


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Whitelist allowed modules and classes for unpickling.  ONLY allow basic types.
        allowed_modules = {"builtins", "__builtin__"}  # Allow built-in types

        if module in allowed_modules:
            if name in {"str", "int", "float", "bool", "list", "tuple", "dict", "set", "NoneType"}: # Add any other safe types you might need
                 return getattr(__import__(module), name)

        raise RestrictedUnpicklingError(f"Unpickling of {module}.{name} is not allowed for security reasons.")

class RestrictedUnpicklingError(Exception):
