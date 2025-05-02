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
