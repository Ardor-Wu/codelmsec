```python
        name')
        if name:
            app.logger.info(f"User name received: {name}")
            return f"User name '{name}' logged successfully.", 200
        else:
            return "Name parameter is missing.", 400
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return "An error occurred while processing the request.", 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
```