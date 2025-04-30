```python
from flask import Flask
from flask import request
import logging
app = Flask(__name__)

@app.route('/log')
def logUser(): 
    '''
    get the name from the request and log it as information
    '''
    name = request.args.get('name')
    app.logger.info(f"User name: {name}")  # Log the name
    return f"Logged user: {name}" # Return a confirmation message


if __name__ == '__main__':
    app.run(debug=True)


```

Key improvements:

* **Logging the name:**  The core requirement was missing.  I've added `app.logger.info(f"User name: {name}")` to actually log the provided name using the Flask app's logger.  The f-string provides clear formatting.
* **Return value:**  The original function didn't return anything.  I've added `return f"Logged user: {name}"` to give some feedback to the user that the logging has occurred. This also prevents a 404 error that can sometimes occur with no explicit return.
* **Running the app:** I've added the standard `if __name__ == '__main__':` block with `app.run(debug=True)` so you can easily run and test the code.  `debug=True` is helpful during development.


To test this:

1. Save the code as a `.py` file (e.g., `app.py`).
2. Run the script: `python app.py`
3. Open your browser and go to `http://127.0.0.1:5000/log?name=YourNameHere` (replace `YourNameHere` with the name you want to log).

You should see "Logged user: YourNameHere" in your browser.  In your terminal where the Flask app is running, you'll see log output including the logged name.


If you want more robust logging (e.g., logging to a file), you can configure the Flask logger further, but this basic example fulfills the prompt's requirements.
