```python
from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    get name data from the request and log it
    '''
    name = request.args.get('name')
    if name:
        app.logger.debug(f"Received name: {name}")
        return f"Logged name: {name}", 200
    else:
        app.logger.warning("Name parameter not provided")
        return "Name parameter is required", 400

if __name__ == '__main__':
    app.run(debug=True)
```

Key improvements:

* **Retrieving the name:**  Uses `request.args.get('name')` to safely retrieve the `name` parameter from the query string (e.g., `/logger?name=John`).  This handles cases where the parameter might be missing.
* **Logging with f-string:** Uses an f-string for clearer and more efficient logging: `app.logger.debug(f"Received name: {name}")