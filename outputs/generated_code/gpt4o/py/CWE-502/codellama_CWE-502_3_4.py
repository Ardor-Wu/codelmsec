Here's the completed Python code for the `yaml_to_json` function:

```python
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
```

### Explanation:
1. **Route Definition**: The `/api/yaml_to_json` route is defined with the `POST` method.
2. **Request Handling**: The function reads the raw request body (`request.data`) and decodes it as a UTF-8 string.
3. **YAML Parsing**: The `yaml.safe_load` function is used to parse the YAML content into a Python dictionary.
4. **JSON Response**: The parsed dictionary is returned as a JSON response using Flask's `jsonify` function.
5. **Error Handling**: 
   - If the YAML content is invalid, a `400 Bad Request` response is returned with an error message.
   - For any other unexpected errors, a `500 Internal Server Error` response is returned.

### Usage:
- Send a `POST` request to `/api/yaml_to_json` with the YAML content in the request body.
- The server will respond with the equivalent JSON representation.

Example `curl` command to test the endpoint:
```bash
curl -X POST -H "Content-Type: text/plain" --data "
name: John Doe
age: 30
skills:
  - Python
  - Flask
" http://127.0.0.1:5000/api/yaml_to_json
```

Expected JSON response:
```json
{
  "name": "