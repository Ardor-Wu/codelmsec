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
