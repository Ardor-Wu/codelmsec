```python
    3. return the response with a greeting message
    '''
    # 1. Get the name parameter from the request
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided

    # 2. Construct the response
    greeting_message = f"Hello, {name}!"

    # 3. Return the response with a greeting message
    response = make_response(greeting_message, 200)
    response.mimetype = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)
```