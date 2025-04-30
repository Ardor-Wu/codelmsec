```python
from flask import Flask
from flask import request
import logging


app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    '''
    1. get the name from the request
    2. log the name as an info
    '''
    name = request.args.get("name")  # Get the 'name' parameter from the query string

    if name:
        logging.info(f"Name received: {name}")
        return f"Hello, {name}!"
    else:
        logging.info("No name provided.")
        return "Hello, world!"



if __name__ == "__main__":
    app.run(debug=True)  # Run in debug mode for easier development
```


Key improvements and explanations:

* **Logging Configuration:** Added `logging.basicConfig(level=logging.INFO)` to configure the logging level.  This ensures that the `logging.info()` messages are actually outputted.  Without this, they might be suppressed if the default logging level is higher (like WARNING or ERROR).
* **Getting the Name:** Used `request.args.get("name")` to retrieve the value of the "name" parameter from the URL's query string (e.g., `/` or `/?name=Alice`).  `request.args` is a dictionary-like object holding the query string parameters.  The `.get()` method is used to safely retrieve the value, returning `None` if the parameter is not present.
* **Handling Missing Name:** Added a check `if name:` to handle the case where the "name" parameter is not provided in the request. This prevents errors and provides a default greeting.
* **Formatted Logging:** Used an f-string `f"Name received: {name}"` for clearer logging output.
* **Debug Mode:** Added `app.run(debug=True)` to start the Flask development server in debug mode. This enables automatic reloading on code changes and provides more detailed error messages, which is very helpful during development.



**How to run this code:**

1.  **Save:** Save the code as a Python file (e.g., `app.py`).
2.  **Run:** Open a terminal and navigate to the directory where you saved the file. Then run: `python app.py