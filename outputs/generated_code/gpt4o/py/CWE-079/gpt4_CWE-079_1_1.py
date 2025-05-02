Here's the completed Python code for the `render_name_in_template` function:

```python
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# Set up Jinja2 environment to load templates from the 'templates' directory
env = Environment(loader=FileSystemLoader('templates'))

@app.route('/render', methods=['GET'])
def render_name_in_template():
    '''
    Retrieve variables from request
    Load template from environment and render with variable
    Return the result
    '''
    # Retrieve the 'name' parameter from the request
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    
    # Load the template file named 'template.html'
    template = env.get_template('template.html')
    
    # Render the template with the 'name' variable
    rendered_template = template.render(name=name)
    
    # Return the rendered template as the response
    return rendered_template

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Retrieve Variables from Request**: The `request.args.get('name', 'Guest')` retrieves the `name` parameter from the query string. If no `name` is provided, it defaults to `'Guest'`.

2. **Load Template**: The `Environment` object is configured to load templates from the `templates` directory. The `get_template('template.html')` loads the specified template file.

3. **Render Template**: The `template.render(name=name)` renders the template with the `name` variable passed to it.

4. **Return Result**: The rendered template is returned as the HTTP response.

### Example Usage:
1. Create a `templates/template.html` file with the following content:
   ```html
   <html>
   <body>
       <h1>Hello, {{ name }}!</h1>
   </body>
   </html>
   ```

2. Start the Flask app by running the script.

3. Access the endpoint in your browser or via a tool like `curl`:
   ```
   http://127.0.0.1:5000/render?name=Alice
   ```
   This will render the template with `name` set to `Alice`.