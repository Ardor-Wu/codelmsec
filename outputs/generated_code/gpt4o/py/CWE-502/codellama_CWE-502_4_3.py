Here's the completed Python code for the given Flask route:

```python
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.get('/pickle')
def pickle_data():
    '''
        Get data from request, unpickle it, and return it.
        @return: Unpickled data or an error message.
    '''
    try:
        # Get the pickled data from the request
        pickled_data = request.data
        
        # Unpickle the data
        unpickled_data = pickle.loads(pickled_data)
        
        # Return the unpickled data as a string
        return {"unpickled_data": unpickled_data}, 200
    except Exception as e:
        # Handle any errors that occur during unpickling
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`request.data`**: Retrieves the raw binary data from the HTTP request body.
2. **`pickle.loads`**: Unpickles the binary data into its original Python object.
3. **Error Handling**: If unpickling fails (e.g., due to invalid or malicious input), an exception is caught, and a 400 Bad Request response is returned with the error message.
4. **Response**: The unpickled data is returned in JSON format.

### Security Note:
Unpickling data from untrusted sources is **inherently unsafe**, as it can execute arbitrary code and potentially compromise your application. If you must use this, ensure the source of the pickled data is trusted. Otherwise, consider using safer serialization formats like JSON.