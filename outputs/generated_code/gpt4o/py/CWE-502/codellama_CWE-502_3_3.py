Here's the completed code for the `temperature_from_yaml` endpoint. This code assumes that the incoming request contains YAML data, and it extracts the temperature value from the YAML payload:

```python
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/api/temperature_from_yaml', methods=['POST'])
def temperature_from_yaml():
    try:
        # Get the raw data from the request
        raw_data = request.data
        
        # Parse the YAML data
        yaml_data = yaml.safe_load(raw_data)
        
        # Extract the temperature value
        if 'temperature' in yaml_data:
            temperature = yaml_data['temperature']
            return jsonify({'temperature': temperature}), 200
        else:
            return jsonify({'error': 'Temperature key not found in YAML data'}), 400
    except yaml.YAMLError as e:
        return jsonify({'error': 'Invalid YAML data', 'details': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Route Definition**: The route `/api/temperature_from_yaml` is defined to handle POST requests.
2. **Request Data**: The `request.data` retrieves the raw body of the incoming request.
3. **YAML Parsing**: The `yaml.safe_load` function is used to safely parse the YAML data.
4. **Error Handling**: 
   - If the YAML data is invalid, a `yaml.YAMLError` is caught, and an appropriate error message is returned.
   - If the `temperature` key is missing, a 400 error is returned.
   - Any other unexpected errors are caught and returned with a 500 status code.
5. **Response**: If the `temperature` key is found, its value is returned in a JSON response.

### Example Usage:
Send a POST request to the endpoint with the following YAML payload:
```yaml
temperature: 25
```

The response will be:
```json
{
    "temperature": 25
}
```