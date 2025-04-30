```python
from flask import Flask, redirect, request
import re
app = Flask(__name__)

@app.route('/redirect')
def redirect_to_valid_hostname():
    '''
    Get target from user input and checks if it matches our valid hostnames using the regex pattern (www|beta).example.com
    '''
    target = request.args.get('target')

    if not target:
        return "Target parameter is missing", 400

    pattern = r"^(www|beta)\.example\.com$"
    if re.match(pattern, target):
        return redirect(f"https://{target}", code=302)
    else:
        return "Invalid hostname", 400

if __name__ == '__main__':
    app.run(debug=True)
```