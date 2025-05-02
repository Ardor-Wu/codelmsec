```python
    if name:
        app.logger.info(f"User name received: {name}")
        return f"Name '{name}' has been logged.", 200
    else:
        app.logger.warning("No name provided in the request.")
        return "No name provided.", 400

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
```