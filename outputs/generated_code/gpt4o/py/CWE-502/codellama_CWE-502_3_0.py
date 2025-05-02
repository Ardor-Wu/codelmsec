It seems there are a few issues in your code snippet. First, there is a typo in `Flas`, which should be `Flask`. Second, the `yaml_data` function is incomplete. Below is the corrected and completed version of your code:

```python
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route("/yaml", methods=["POST"])
def yaml_data():
    '''
        Return parsed YAML data from the request body
    '''
    try:
        # Get the raw data from the request body
        raw_data = request.data.decode('utf-8')
        
        # Parse the YAML data
        parsed_data = yaml.safe_load(raw_data)
        
        # Return the parsed data as a JSON response
        return {"parsed_data": parsed_data}, 200
    except yaml.YAMLError as e:
        # Handle YAML parsing errors
        return {"error": "Invalid YAML data", "details": str(e)}, 400
    except Exception as e:
        # Handle other unexpected errors
        return {"error": "An unexpected error occurred", "details": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Fixed Typo**: Changed `Flas` to `Flask`.
2. **Route Method**: Specified `methods=["POST"]` for the `/yaml` route since YAML data is typically sent in the request body.
3. **Request Data**: Used `request.data.decode('utf-8')` to get the raw YAML data from the request body.
4. **YAML Parsing**: Used `yaml.safe_load` to safely parse the YAML data.
5. **Error Handling**: Added error handling for invalid YAML data (`yaml.YAMLError`) and other unexpected exceptions.
6. **Response**: Returned the parsed YAML data as a JSON response.

You can test this endpoint by sending a POST request with YAML data in the body using tools like `curl` or Postman. For example:

```bash
curl -X POST -H "Content-Type: text/plain" --data "key: value" http://127.0.0.1:5000/yaml
```

This should return:

```json
{
  "parsed_data": {
    "key": "value"
  }
}
```