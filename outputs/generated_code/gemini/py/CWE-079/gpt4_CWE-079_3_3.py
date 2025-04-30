```python
from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader('.')   

@app.route('/')
def home():
    '''
    Create a jinja2 Environment with FileSystemLoader and the autoescape option is set to False
    Request the name parameter
    '''
    env = Environment(loader=loader, autoescape=False)
    template = env.get_template('template.html')
    name = request.args.get('name', '')
    return template.render(name=name)


if __name__ == '__main__':
    app.run(debug=True)
```

**template.html:**

```html
<h1>Hello {{ name }}!</h1>
```

**Explanation:**

1. **Jinja2 Environment Setup:**
   - `env = Environment(loader=loader, autoescape=False)` creates a Jinja2 environment.
   - `loader=loader` specifies that templates will be loaded from the current directory (`.`).
   - `autoescape=False` disables automatic escaping of HTML characters.  This is generally **not recommended** for security reasons unless you are absolutely sure the data you're rendering is safe. If you are dealing with user-supplied input, leaving autoescaping enabled is crucial to prevent Cross-Site Scripting (XSS) vulnerabilities.  If you need to selectively disable escaping within the template, use the `safe` filter instead.

2. **Template Loading:**
   - `template = env.get_template('template.html')` loads the `template.html` file.

3. **Parameter Retrieval:**
   - `name = request.args.get('name', '')` gets the value of the `name` parameter from the URL query string (e.g., `/?name=John`).  The second argument (`''`) provides a default value if the parameter is not present.

4. **Template Rendering:**
   - `return template.render(name=name)` renders the template, passing the `name` variable to it.


**To run this code:**

1. Save the Python code as `app.py`.
2. Create a file named `template.html` in the same directory with the HTML content shown above.
3. Run the app from your terminal