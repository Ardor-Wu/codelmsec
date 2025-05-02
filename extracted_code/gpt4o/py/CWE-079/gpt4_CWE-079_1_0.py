# Get the 'name' parameter from the request arguments
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided

    # Set up Jinja2 environment to load templates from the 'templates' directory
    env = Environment(loader=FileSystemLoader('templates'))

    # Load the specific template file
    template = env.get_template('greeting.html')

    # Render the template with the provided name
    rendered_html = template.render(name=name)

    # Return the rendered HTML response
    return rendered_html

if __name__ == '__main__':
    app.run(debug=True)
