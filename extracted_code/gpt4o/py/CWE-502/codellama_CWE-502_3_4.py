from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route("/api/yaml_to_json", methods=["POST"])
def yaml_to_json():
    """
    Convert YAML to JSON.
    Expects YAML content in the POST request body.
    Returns the converted JSON.
    """
    try:
        # Get the YAML content from the request body
        yaml_content = request.data.decode("utf-8")
        
        # Parse the YAML content
        yaml_data = yaml.safe_load(yaml_content)
        
        # Return the parsed YAML as JSON
        return jsonify(yaml_data), 200
    except yaml.YAMLError as e:
        # Handle YAML parsing errors
        return jsonify({"error": "Invalid YAML format", "details": str(e)}), 400
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
