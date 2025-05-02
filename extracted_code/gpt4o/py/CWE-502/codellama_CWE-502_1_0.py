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
