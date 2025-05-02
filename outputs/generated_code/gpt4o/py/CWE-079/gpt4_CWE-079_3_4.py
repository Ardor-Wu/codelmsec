Here is the completed Python code for the `rendered_response` function:

```python
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
```

### Explanation:
1. **Template Loading**: The `env.get_template('index.html')` loads the `index.html` template from the `templates/` directory.
2. **Context Variables**: A dictionary `context` is passed to the `template.render()` method to populate dynamic content in the template.
3. **Response Creation**: The `make_response()` function creates a response object with the rendered HTML.
4. **Content-Type Header**: The `Content-Type` header is explicitly set to `text/html` to indicate the response contains HTML content.

Make sure you have an `index.html` file in the `templates/` directory for this code to work. Here's an example of what the `index.html` file might look like:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```