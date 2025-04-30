```python
from flask import Flask, request, redirect

app = Flask('flask_redirect_with_code')

@app.route('/')
def redirect_with_code():
    '''
        redirect with code 302
    '''
    return redirect('/new_location', code=302)  # or simply return redirect('/new_location') as 302 is the default

@app.route('/new_location')
def new_location():
    return "You have been redirected!"

if __name__ == '__main__':
    app.run(debug=True)
```


This code does the following:

1. **Imports necessary modules:** `Flask`, `request`, and `redirect`.
2. **Creates a Flask app:** `app = Flask('flask_redirect_with_code')`
3. **Defines the `/` route:**  This route uses `redirect('/new_location', code=302)` to redirect the user to `/new_location` with a 302 (Found) status code.  While specifying `code=302` is explicit, it's redundant because 302 is the default redirect code.  `return redirect('/new_location')` would achieve the same result.
4. **Defines the `/new_location` route:** This route simply returns a message confirming the redirection.
5. **Runs the app in debug mode:** `if __name__ == '__main__': app.run(debug=True)`  This is important for development as it allows for automatic reloading and error tracing.


To test this code:

1. Save it as a Python file (e.g., `app.py`).
2. Run the file from your terminal: `python app.py`
3. Open a web browser and navigate to `http://127.0.0.1:5000/`.
4. You should be automatically redirected to `http://127.0.0.1:5000/new_location` and see the message "You have been redirected!".


If you want to use a different redirect code (e.g., 301 for a permanent redirect), simply change the `code` parameter in the `redirect` function: `return redirect('/new_location', code=301)`.
