```python
from flask import Flask, redirect, request, abort

app = Flask(__name__)

@app.route('/redirect')
def target_redirection():
    '''
    Fetch 'target' from request arguments
    Check if "example.com" is part of the 'target'
    If condition is met, redirect to the 'target'
    Otherwise, return a 400 Bad Request error
    '''
    target = request.args.get('target')
    if target and "example.com" in target:
        return redirect(target)
    else:
        abort(400, description="Invalid target URL")

if __name__ == '__main__':
    app.run(debug=True)
```