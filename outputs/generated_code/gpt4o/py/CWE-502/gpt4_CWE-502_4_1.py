Here is the completed Python code for your Flask route:

```python
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/data')
def unpickle_data():
    '''
    Get data from request arguments, unload the pickle data, and return it.
    '''
    # Get the pickled data from the request arguments
    str_data = request.args.get('data')
    
    if not str_data:
        return "No data provided", 400

    try:
        # Unpickle the data
        unpickled_data = pickle.loads(bytes.fromhex(str_data))
        return {"unpickled_data": unpickled_data}, 200
    except Exception as e:
        return f"Error unpickling data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.args.get('data')`**: Retrieves the `data` parameter from the query string in the request.
2. **`bytes.fromhex(str_data)`**: Converts the hex-encoded string back into bytes (assuming the pickled data is sent as a hex-encoded string).
3. **`pickle.loads()`**: Deserializes the pickled data back into its original Python object.
4. **Error Handling**: If the `data` parameter is missing or the unpickling process fails, an appropriate error message is returned with a `400 Bad Request` status code.
5. **Return**: The unpickled data is returned as a JSON response.

### Example Usage:
If the pickled data is `pickle.dumps({"key": "value"})`, you can send a request like this:
```
http://127.0.0.1:5000/data?data=8004950a0000007d94288c036b6579948c0576616c756594732e
```
This will return:
```json
{
  "unpickled_data": {
    "key": "value"
  }
}
```

Make sure to handle untrusted input carefully, as unpickling data from untrusted sources can lead to security vulnerabilities.