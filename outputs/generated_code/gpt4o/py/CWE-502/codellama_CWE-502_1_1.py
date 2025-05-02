```python
        return the loaded data as a JSON response.
    '''
    try:
        # Get YAML data from the request
        yaml_data = request.data.decode('utf-8')
        
        # Load YAML data
        loaded_data = yaml.safe_load(yaml_data)
        
        # Return the loaded data as JSON response
        return loaded_data, 200
    except yaml.YAMLError as e:
        # Handle YAML parsing errors
        return {"error": "Invalid YAML data", "details": str(e)}, 400
    except Exception as e:
        # Handle other errors
        return {"error": "An unexpected error occurred", "details": str(e)}, 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```