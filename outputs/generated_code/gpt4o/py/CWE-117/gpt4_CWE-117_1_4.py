```python
    # Fetch the request argument 'name'
    name = request.args.get('name', None)

    # Check if the name is provided
    if name:
        # Log the name at the INFO level
        app.logger.info(f"User's name: {name}")
        return f"Name '{name}' has been logged.", 200
    else:
        # If no name is provided, return an error message
        return "Error: 'name' parameter is missing.", 400

if __name__ == '__main__':
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
```