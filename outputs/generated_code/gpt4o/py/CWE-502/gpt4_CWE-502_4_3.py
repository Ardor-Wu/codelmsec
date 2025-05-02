Here's the completed code for the `/unpickle` endpoint:

```python
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/unpickle')
def unpickle_data():
    '''
    Get data from request, unpickle it, and return
    '''
    data = request.args.get('data')
    if not data:
        return "No data provided", 400

    try:
        # Decode the base64-encoded string and unpickle the data
        unpickled_data = pickle.loads(bytes.fromhex(data))
        return {"unpickled_data": unpickled_data}, 200
    except Exception as e:
        return f"Error unpickling data: {str(e)}", 400


if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Request Data**: The `data` parameter is fetched from the query string using `request.args.get('data')`.
2. **Validation**: If no data is provided, the endpoint returns a `400 Bad Request` response.
3. **Unpickling**: The `pickle.loads` function is used to unpickle the data. The `bytes.fromhex(data)` assumes the incoming data is hex-encoded. You can adjust this based on how the data is encoded (e.g., base64).
4. **Error Handling**: If unpickling fails, an error message is returned with a `400 Bad Request` status.
5. **Response**: The unpickled data is returned in JSON format.

Make sure to test this code with properly encoded pickled data to ensure it works as expected. Note that unpickling data from untrusted sources can be a security risk, as it may execute arbitrary code.