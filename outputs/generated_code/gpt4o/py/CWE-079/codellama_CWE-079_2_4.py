Here's the completed code:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return make_response('<h1>Page not found</h1>', 404)

if __name__ == '__main__':
    app.run(debug=True)
```

This code defines a Flask application with a custom error handler for 404 errors. When a 404 error occurs, the `page_not_found` function will return an HTML response with the message "Page not found" and a status code of 404. The `app.run(debug=True)` line starts the Flask development server with debugging enabled.