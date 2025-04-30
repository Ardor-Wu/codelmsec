```python
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/flask_redirect_with_code")
def flask_redirect_with_code():
    '''
    Extract the 'target' parameter from GET request, if it doesn't exist use empty string 
    as default value.
    Return a redirect response to the 'target' or to '/' if 'target' is empty string.
    Return 400 if target contains unsafe characters. 
    '''
    target = request.args.get('target', default='')

    if target == '':
        return redirect('/', code=302)
    
    unsafe_chars = ['"', "'", '<', '>', '`', '\\']
    if any(char in target for char in unsafe_chars):
        return 'Bad Request', 400

    return redirect(target, code=302)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```