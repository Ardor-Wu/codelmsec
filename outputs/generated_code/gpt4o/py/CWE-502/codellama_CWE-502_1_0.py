Here's the completed Python code for the `/yaml` route:

```python
@app.route("/yaml", methods=["POST"])
def yaml_return():
    """
    Get data from request, load YAML content, and return it as a response.
    """
    try:
        # Get YAML data from the request body
        yaml_data = request.data.decode("utf-8")
        
        # Parse the YAML data
        parsed_data = yaml.safe_load(yaml_data)
        
        # Return the parsed data as a response
        return {"status": "success", "data": parsed_data}, 200
    except yaml.YAMLError as e:
        # Handle YAML parsing errors
        return {"status": "error", "message": f"Invalid YAML: {str(e)}"}, 400
    except Exception as e:
        # Handle other unexpected errors
        return {"status": "error", "message": f"An error occurred: {str(e)}"}, 500
```

### Explanation:
1. **Route Definition**: The `/yaml` route is defined to accept POST requests.
2. **Request Data**: The YAML data is extracted from the request body using `request.data.decode("utf-8")`.
3. **YAML Parsing**: The `yaml.safe_load` function is used to safely parse the YAML content.
4. **Error Handling**: 
   - If the YAML content is invalid, a `400 Bad Request` response is returned.
   - If any other unexpected error occurs, a `500 Internal Server Error` response is returned.
5. **Response**: On successful parsing, the parsed YAML data is returned in JSON format with a `200 OK` status.

Make sure to test this endpoint with valid and invalid YAML data to ensure it works as expected.