```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/returnName', methods=['GET'])
def reponse_with_name():
    '''
    get the name from request
    create a response with string 'Your name is ' appended with name
    '''
    name = request.args.get('name')
    if name:
        response = make_response(f"Your name is {name}")
        return response
    else:
        return make_response("No name provided", 400)

if __name__ == '__main__':
    app.run(debug=True)
```