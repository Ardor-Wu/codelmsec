```python
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render_template')
def render_from_template():
    """
    Gets the name from the request,
    renders it using Jinja2 template and returns the HTML response.
    """
    name = request.args.get('name', 'World')  # Default to 'World' if name is not provided

    # Create a Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))

    # Load the template
    template = env.get_template('template.html')

    # Render the template with the name
    html = template.render(name=name)

    return html

# Example template file (template.html):
# <h1>Hello, {{ name }}!</h1>


if __name__ == '__main__':
    app.run(debug=True)

```

**Explanation and improvements:**

1. **Get the name from the request:**
   - `name = request.args.get('name', 'World')` retrieves the `name` parameter from the URL query string (e.g., `/render_template?name=John`).
   - It defaults to `'World'` if the `name` parameter is not provided, preventing errors.

2. **Jinja2 Environment and Loader:**
   - `env = Environment(loader=FileSystemLoader('.'))` creates a Jinja2 environment and configures it to load templates from the current directory (`.`).  You can change this to a specific templates folder if needed.

3. **Load and Render the Template:**
   - `template = env.get_template('template.html')` loads the `template.html` file.
   - `html = template.render(name=name)` renders the template, passing the `name` variable to it.  Jinja2 uses `{{ name }}` to substitute the value within the template.

4. **Return the HTML:**
   - `return html` sends the rendered HTML back to the client.

5. **Example Template (template.html):**
   - You need to create a file named `template.html` in the same directory as your Python script with the following content (or similar):

   ```html
   <h1>Hello, {{ name }}!