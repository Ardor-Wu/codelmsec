```python
from flask import Flask, redirect, request
app = Flask(__name__)

@app.route('/handler')
def handle_redirection():
    '''
    get target URL from request. The second parameter in the get 
    method provides a default value if 'target'
    doesn't exist
    '''
    target_url = request.args.get('target', 'https://www.example.com')
    return redirect(target_url)

if __name__ == '__main__':
    app.run(debug=True)
```