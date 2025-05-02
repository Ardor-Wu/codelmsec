```python
    # get 'name' from the request arguments
    name = request.args.get('name', default=None)

    # Check if the name parameter is provided
    if name:
        # Log the name
        app.logger.info(f"Received name: {name}")
        return f"Hello, {name}!", 200
    else:
        # Log the missing name
        app.logger.warning("No name parameter provided in the request.")
        return "Error: 'name' parameter is missing.", 400

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
```