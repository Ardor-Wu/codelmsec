'''
    name = request.args.get('name', 'Guest')  # Get the 'name' parameter from the query string, default to 'Guest'
    escaped_name = escape(name)  # Escape the name to prevent XSS attacks
    template = env.get_template('home.html')  # Load the 'home.html' template from the 'templates' directory
    return template.render(name=escaped_name)  # Render the template with the escaped name
