Here's the completed Python code:

```python
from flask import request, current_app, Flask
import logging

logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)

@app.route('/logger/input', methods=['POST'])
def log_input():
    '''
    Get input data from the request and log it as an error
    '''
    user_input = request.get_json()  # Assuming the input is sent as JSON
    if not user_input:
        return {"error": "No input data provided"}, 400

    current_app.logger.error(f"User input logged as error: {user_input}")
    return {"message": "Input logged successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.get_json()`**: This retrieves the JSON payload from the incoming request. If the request doesn't contain valid JSON, it will return `None`.
2. **Logging**: The `current_app.logger.error` method is used to log the input data as an error.
3. **Error Handling**: If no input data is provided, the server responds with a 400 status code and an error message.
4. **Route Method**: The route is configured to accept `POST` requests since we're expecting input data.

Make sure to send a `POST` request with a JSON payload to `/logger/input` when testing this endpoint. For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/logger/input
```