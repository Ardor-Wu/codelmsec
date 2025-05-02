It looks like you're trying to create a Flask application with a route that processes YAML data. Below is the corrected and completed code:

```python
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/load_yaml', methods=['GET'])
def load_yaml():
    """
    A Flask route that loads YAML data from a query parameter and returns it as JSON.
    """
    # Get the 'pickled' query parameter from the request
    pickled = request.args.get('pickled')

    if not pickled:
        return jsonify({"error": "Missing 'pickled' query parameter"}), 400

    try:
        # Parse the YAML data
        yaml_data = yaml.safe_load(pickled)
        return jsonify({"parsed_yaml": yaml_data}), 200
    except yaml.YAMLError as e:
        return jsonify({"error": "Invalid YAML data", "details": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation of Changes:
1. **Fixed the `Flas` typo**: Changed `Flas` to `Flask`.
2. **Added a route**: Specified the route `/load_yaml` and allowed only `GET` requests.
3. **Implemented query parameter handling**: Used `request.args.get('pickled')` to retrieve the `pickled` query parameter.
4. **Error handling**: Added checks for missing or invalid YAML data.
5. **Returned JSON responses**: Used `jsonify` to return structured responses.

### Usage:
Start the Flask application, and access the `/load_yaml` route with a `pickled` query parameter containing YAML data. For example:

```
http://127.0.0.1:5000/load_yaml?pickled=key:value
```

This will parse the YAML data and return it as JSON.