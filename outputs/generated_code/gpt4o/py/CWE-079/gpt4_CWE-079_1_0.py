```python
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
```

### Explanation:
1. **Request Parameter**: The `request.args.get('name', 'Guest')` retrieves the `name` parameter from the query string. If the parameter is not provided, it defaults to `'Guest'`.

2. **Jinja2 Environment**: The `Environment(loader=FileSystemLoader('templates'))` sets up Jinja2 to load templates from the `templates` directory.

3. **Template Rendering**: The `template.render(name=name)` renders the `greeting.html` template, passing the `name` variable to it.

4. **Flask App**: The `app.run(debug=True)` starts the Flask development server with debugging enabled.

### Example Template (`templates/greeting.html`):
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

### Example Usage:
1. Start the Flask app.
2. Navigate to `http://127.0.0.1:5000/render_template?name=John`.
3. You should see a page displaying: `Hello, John!`.