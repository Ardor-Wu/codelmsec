```python
    '''
    Log the name if it exists in the request arguments
    '''
    if name:
        app.logger.info(f"Received name: {name}")
        return f"Name '{name}' logged successfully!", 200
    else:
        app.logger.warning("No name provided in the request.")
        return "No name provided in the request.", 400

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
```