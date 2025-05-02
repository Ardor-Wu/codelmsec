```python
    '''
    get a name (param) from request
    open the shared.html file and read it to html
    replace placeholder {{name}} on html using the provided name
    return the modified HTML as a response
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided

    # Open and read the shared.html file
    try:
        with open('shared.html', 'r') as file:
            html = file.read()
    except FileNotFoundError:
        return make_response("shared.html file not found", 404)

    # Replace the placeholder {{name}} with the provided name
    modified_html = html.replace('{{name}}', name)

    # Return the modified HTML as a response
    response = make_response(modified_html)
    response.headers['Content-Type'] = 'text/html'
    return response
```