```python
from flask import Flask, request, make_response

app = Flask( __name__ )

@app.get('/hello')
def hello():
    '''
    1. get the name parameter from request
    2. construct the response
    3. return the response
    '''
    name = request.args.get('name', 'World')  # Get 'name' from query parameters, default to 'World'
    response = make_response(f"Hello, {name}!")  # Create a response object
    return response

if __name__ == '__main__':
    app.run(debug=True)
```