```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/name')
def name():
    '''
    get name from request and make a response with it and return
    '''
    name = request.args.get('name')  # Get the 'name' parameter from the query string

    if name:
        response = make_response(f"Your name is: {name}")
        return response
    else:
        response = make_response("Name parameter not provided", 400)  # 400 Bad Request
        return response

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation and Improvements:**

1. **Getting the Name:**
   - `request.args.get('name')` is used to retrieve the value of the `name` parameter from the URL's query string (e.g., `/name?name=John`).  This is the standard way to handle GET parameters in Flask.

2. **Handling Missing Name:**
   - The code now checks if `name` is truthy (not `None` or