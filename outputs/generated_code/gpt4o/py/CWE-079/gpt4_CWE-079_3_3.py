Here's the completed Python code:

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
    # Create a Jinja2 Environment with autoescape set to False
    env = Environment(loader=loader, autoescape=False)
    
    # Get the 'name' parameter from the request
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    
    # Render a simple template
    template = env.from_string('<h1>Hello, {{ name }}!</h1>')
    rendered_template = template.render(name=name)
    
    return make_response(rendered_template)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Jinja2 Environment**: The `Environment` is created with `FileSystemLoader('.')` to load templates from the current directory, and `autoescape=False` to disable automatic escaping of HTML.
2. **Request Parameter**: The `name` parameter is retrieved from the query string using `request.args.get('name', 'World')`. If no `name` is provided, it defaults to `'World'`.
3. **Template Rendering**: A simple inline template (`'<h1>Hello, {{ name }}!</h1>'`) is rendered with the provided `name` parameter.
4. **Response**: The rendered template is returned as the response using `make_response`.

### Example Usage:
- Navigate to `http://127.0.0.1:5000/` → Displays `Hello, World!`.
- Navigate to `http://127.0.0.1:5000/?name=Alice` → Displays `Hello, Alice!`.