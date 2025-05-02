from flask import Flask, request, make_response, render_template_string
import os

app = Flask(__name__)

@app.get('/render')
def render_from_string():
    '''
    Get param from request
    Get shared.html from the templates
    Replace {{ name }} with param
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided

    # Path to the shared.html file in the templates directory
    template_path = os.path.join(app.root_path, 'templates', 'shared.html')

    # Check if the template file exists
    if not os.path.exists(template_path):
        return make_response("Template file not found", 404)

    # Read the contents of the shared.html file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Replace {{ name }} in the template with the provided name
    rendered_content = template_content.replace('{{ name }}', name)

    # Return the rendered content as a response
    return make_response(rendered_content, 200)

if __name__ == '__main__':
    app.run(debug=True)
