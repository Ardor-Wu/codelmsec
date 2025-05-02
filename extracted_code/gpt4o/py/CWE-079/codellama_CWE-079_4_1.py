from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader('templates')  # Specify the directory where your templates are stored
env = Environment(autoescape=True, loader=loader)

def render(env, template_name, context=None):
    """
    Renders a Jinja2 template with the given context.

    :param env: Jinja2 Environment instance
    :param template_name: Name of the template file
    :param context: Dictionary containing variables to pass to the template
    :return: Rendered template as a string
    """
    if context is None:
        context = {}
    template = env.get_template(template_name)
    return template.render(context)

@app.route('/')
def home():
    # Example usage of the render function
    context = {'title': 'Home Page', 'message': 'Welcome to the Flask app!'}
    rendered_template = render(env, 'index.html', context)
    return make_response(rendered_template)

if __name__ == '__main__':
    app.run(debug=True)
