```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/response', methods =['GET'])
def get_response():
    '''
    Fetch data "name" from request
    Try to concatenate given data to string
    Make a response from
    '''
    try:
        name = request.args.get('name')
        response_string = "Hello, " + name + "!"
        response = make_response(response_string)
        return response
    except TypeError:
        return make_response("Please provide the 'name' parameter.", 400)


if __name__ == '__main__':
    app.run(debug=True)
```