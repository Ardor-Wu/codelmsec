```python
from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader('templates/')
env = Environment(loader=loader, autoescape=select_autoescape(['html', 'xml']))

@app.route('/index')
def rendered_response():
    '''
    Use a template to render the response.
    '''
    template = env.get_template('index.html')
    name = request.args.get('name', 'World') # Use default name if no name is provided
    return make_response(template.render(name=escape(name)))


if __name__ == "__main__":
    app.run(debug=True)

```

**templates/index.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Index</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

**Explanation:**

1. **Import necessary modules:** `Flask`, `request`, `make_response`, `escape` from `flask`, and `Environment`, `select_autoescape`, `FileSystemLoader` from `jinja2`.

2. **Initialize Flask app and Jinja2 environment:**
   - `app = Flask(__name__)` creates a Flask app instance.
   - `loader = FileSystemLoader('templates/')` specifies the directory where templates are located.
   - `env = Environment(...)` sets up the Jinja2 environment with the loader and autoescape for HTML and XML files (for security).

3. **Define the route:** `@app.route('/index')` registers the `rendered_response` function to handle requests to the `/index` URL.

4. **Get the template:** `template = env.get_template('index.html')` loads the `index.html` template.

5. **Get the name parameter:** `name = request.args.get('name', 'World')` retrieves the `name` parameter from the request's query string. If the parameter is not present, it defaults to 'World'.  **Crucially, we use `escape(name)` to prevent XSS vulnerabilities.**

6. **Render and return the response:** `return make