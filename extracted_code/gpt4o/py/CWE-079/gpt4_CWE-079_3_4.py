@app.route('/index')
def rendered_response():
    '''
    Use Jinja2 to render an HTML template and return the response.
    '''
    # Load the template named 'index.html' from the 'templates/' directory
    template = env.get_template('index.html')

    # Render the template with some context variables
    context = {
        'title': 'Welcome to My Website',
        'message': 'Hello, Flask and Jinja2!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    rendered_html = template.render(context)

    # Create a response object with the rendered HTML
    response = make_response(rendered_html)

    # Set the content type to 'text/html'
    response.headers['Content-Type'] = 'text/html'

    return response
