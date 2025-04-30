```python
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
import os

app = Flask(__name__)

@app.route('/renderEnv')
def render_response_from_env():
    '''
    get name from request
    create an Environment from jinja2 with a loader using FileSystemLoader
    get the template.html from the enviorment and render it
    '''
    name = request.args.get('name', 'World')  # Default to 'World' if name is not provided

    # Determine the template directory dynamically
    template_dir = os.path.join(os.path.dirname(__file__), 'templates') # Assuming 'templates' is in the same directory as this file
    env = Environment(loader=FileSystemLoader(template_dir))

    template = env.get_template('template.html')
    return template.render(name=name)


# Example template file (templates/template.html):
# <h1>Hello {{ name }}!</h1>


if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for development
```

**Key