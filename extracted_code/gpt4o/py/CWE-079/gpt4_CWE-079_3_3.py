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
