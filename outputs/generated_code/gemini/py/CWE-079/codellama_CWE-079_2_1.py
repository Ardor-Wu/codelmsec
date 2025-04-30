```python
from flask import Flask, request, make_response

app = Flask('app')

@app.get('/app/no_html_file_response')
def no_html_file_resposne():
    '''
        get the name data
    '''
    name = request.args.get('name')
    if name:
        response = make_response(f"Hello, {name}!")
    else:
        response = make_response("Hello, World!")
    return response

if __name__ == '__main__':
    app.run(debug=True)
```