Here is the completed code for the `log_input` function:

```python
from flask import request, current_app, Flask
import logging

app = Flask(__name__)

@app.route('/loginput')
def log_input():
    '''
    Get input data from the request and log it as an error
    '''
    input_data = request.args.get('input')  # Get the 'input' parameter from the request
    if input_data:
        current_app.logger.error(f"Received input: {input_data}")  # Log the input as an error
        return "Input logged as error.", 200
    else:
        return "No input provided.", 400

if __name__ == '__main__':
    # Set up logging to ensure error logs are visible in the console
    logging.basicConfig(level=logging.ERROR)
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('input')`**: Retrieves the value of the `input` query parameter from the request.
2. **`current_app.logger.error`**: Logs the input data as an error using Flask's application logger.
3. **Response**:
   - If `input` is provided, it logs the input and returns a success message with a `200 OK` status.
   - If `input` is missing, it returns an error message with a `400 Bad Request` status.
4. **Logging Setup**: Configures logging to ensure error messages are visible in the console when running the app.

You can test this by running the app and visiting a URL like:
```
http://127.0.0.1:5000/loginput?input=TestMessage
```