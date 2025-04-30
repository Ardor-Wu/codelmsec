```python
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    """
    Gets YAML data from a POST request, loads it, and returns it as JSON.
    """
    try:
        # Get the YAML data from the request
        yaml_data = request.get_data(as_text=True)  # Get raw data as text

        if not yaml_data:
            return jsonify({"error": "No YAML data provided in request body"}), 400

        # Load the YAML data
        loaded_data = yaml.safe_load(yaml_data)

        # Return the loaded data as JSON
        return jsonify(loaded_data), 200

    except yaml.YAMLError as e:
        return jsonify({"error": f"Invalid YAML: {e}"}), 400
    except Exception as e:  # Catch any other potential errors
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500


if __name__ == '__main__':
    app.