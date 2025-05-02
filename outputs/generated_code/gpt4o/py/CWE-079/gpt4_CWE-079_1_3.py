templates from the 'templates' directory, render the template with the provided 'name', and return the rendered HTML.
    '''
    # Get the 'name' parameter from the request arguments
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided

    # Setup Jinja2 environment to load templates from the 'templates' directory
    env = Environment(loader=FileSystemLoader('templates'))

    # Load the template file (e.g., 'greeting.html')
    template = env.get_template('greeting.html')

    # Render the template with the provided 'name'
    rendered_html = template.render(name=name)

    # Return the rendered HTML
    return rendered_html


if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Request Argument**: The `name` parameter is fetched from the request arguments using `request.args.get()`. If no `name` is provided, it defaults to `'Guest'`.
2. **Jinja2 Environment**: The `Environment` is configured to load templates from the `templates` directory.
3. **Template Rendering**: The `greeting.html` template is loaded and rendered with the `name` variable passed to it.
4. **Flask App**: The app runs in debug mode for easier development and debugging.

### Example `greeting.html` Template:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Greeting</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

### Usage:
1. Place the `greeting.html` file in a `templates` directory in the same folder as the Python script.
2. Start the Flask app and visit `http://127.0.0.1:5000/template?name=YourName` in your browser. Replace `YourName` with any name you'd like to see rendered.