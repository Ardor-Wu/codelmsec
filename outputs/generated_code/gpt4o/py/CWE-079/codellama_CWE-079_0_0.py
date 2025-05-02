Here's the completed Python code for your Flask route:

```python
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
```

### Explanation:
1. **Request Parameter**: The `name` parameter is fetched from the query string using `request.args.get('name')`. If no parameter is provided, it defaults to `'Guest'`.
2. **Template File**: The `shared.html` file is read from the `templates` directory.
3. **String Replacement**: The `{{ name }}` placeholder in the template is replaced with the value of the `name` parameter.
4. **Response**: The rendered content is returned as an HTTP response.

### Example Usage:
If you run the Flask app and visit `http://127.0.0.1:5000/render?name=John`, the app will render the `shared.html` file with `{{ name }}` replaced by `John`.

Make sure you have a `shared.html` file in the `templates` directory for this to work. For example:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```