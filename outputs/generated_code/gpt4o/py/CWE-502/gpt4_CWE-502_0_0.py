Here's the completed Python code for the `unpickle_data` function:

```python
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/unpickle_data')
def unpickle_data():
    '''
    Get data from request, un-pickle it and return the result
    '''
    try:
        # Get the data from the request
        data = request.args.get('data')
        
        # Decode the data from base64 (if necessary) and unpickle it
        unpickled_data = pickle.loads(bytes.fromhex(data))
        
        # Return the unpickled data as a string
        return str(unpickled_data)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Request Data**: The `data` parameter is fetched from the query string using `request.args.get('data')`.
2. **Unpickling**: The `pickle.loads()` function is used to unpickle the data. The `bytes.fromhex(data)` is used to convert the hex-encoded string back into bytes before unpickling.
3. **Error Handling**: A `try-except` block is added to handle any errors that might occur during unpickling (e.g., invalid or malicious input).
4. **Return Value**: The unpickled data is converted to a string and returned as the response.

### Security Note:
Unpickling data from untrusted sources is **extremely dangerous** because it can execute arbitrary code. If this endpoint is exposed to external users, it can lead to severe security vulnerabilities. Consider using a safer serialization format like JSON or validating the input thoroughly before unpickling.