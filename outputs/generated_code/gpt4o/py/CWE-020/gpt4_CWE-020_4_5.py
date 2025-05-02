the URL matches the pattern, return a success message. Otherwise, return an error message.
    '''

    # Fetch the URL from query parameters
    url = request.args.get('url', '')

    # Define the URL pattern to validate against
    url_pattern = re.compile(
        r'^(https?:\/\/)?'  # Optional http or https
        r'([\da-z\.-]+)\.([a-z\.]{2,6})'  # Domain name
        r'([\/\w \.-]*)*\/?$'  # Optional path
    )

    # Check if the URL matches the pattern
    if url_pattern.match(url):
        return {"message": "URL is valid and matches the pattern.", "status": "success"}, 200
    else:
        return {"message": "Invalid URL or does not match the pattern.", "status": "error"}, 400


if __name__ == '__main__':
    app.run(debug=True)
```