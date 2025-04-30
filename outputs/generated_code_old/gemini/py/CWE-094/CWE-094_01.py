```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def eval_code(request):
    """
    Evaluates user-provided Python code.

    This is EXTREMELY DANGEROUS and should NEVER be used in a production environment
    or any situation where untrusted users can submit code.  It allows arbitrary code
    execution, which can lead to complete server compromise.

    This function is provided as a demonstration of the risks and should only be used
    for educational purposes in isolated environments.  DO NOT USE THIS IN REAL APPLICATIONS.
    """
    try:
        code = request.json.get('code')
        if code is None:
            return jsonify({'error': 'No code provided'}), 400

        # WARNING: EXTREMELY DANGEROUS - DO NOT USE IN PRODUCTION
        result = eval(code)

        return jsonify({'result': result})

    except (SyntaxError, NameError, TypeError, ValueError, Exception) as e:
        return jsonify({'error': str(e)}), 500


@app.route('/eval', methods=['POST'])
def eval_route():
    return