Here's the completed code:

```python
from flask import request, Flask
import pickle

app = Flask(__name__)

@app.route('/pickle_load')
def load_pickle_data():
    '''
    Retrieve data from request, un-pickle it using pickle.loads() and return the resulted
    data
    '''
    data = request.args.get('data')
    if data is None:
        return "No data provided", 400
    
    try:
        # Decode the data from a string to bytes and unpickle it
        unpickled_data = pickle.loads(bytes(data, 'utf-8'))
        return str(unpickled_data), 200
    except Exception as e:
        return f"Error unpickling data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Retrieve Data**: The `request.args.get('data')` retrieves the `data` parameter from the query string.
2. **Check for None**: If no data is provided, return a 400 Bad Request response.
3. **Unpickle Data**: The `pickle.loads()` function is used to unpickle the data. Since `request.args.get()` returns a string, it is converted to bytes using `bytes(data, 'utf-8')`.
4. **Error Handling**: If an error occurs during unpickling, it is caught and a 400 response is returned with the error message.

### Note:
- Ensure that the data being sent to this endpoint is properly encoded and safe to unpickle. Unpickling data from untrusted sources can lead to security vulnerabilities.