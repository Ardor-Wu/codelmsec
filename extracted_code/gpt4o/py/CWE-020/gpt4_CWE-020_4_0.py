'''
    get url from request
    applying a regular expression to it
    then verify if it is a valid URL
    '''
    # Extract the URL from the request arguments
    url = request.args.get('url', '')

    # Define a regular expression for validating a URL
    url_regex = re.compile(
        r'^(https?:\/\/)?'  # Optional scheme (http or https)
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Top-level domain
        r'(\/[^\s]*)?$'  # Optional path
    )

    # Check if the URL matches the regular expression
    if url_regex.match(url):
        return {"valid": True, "message": "The URL is valid."}, 200
    else:
        return {"valid": False, "message": "The URL is invalid."}, 400

if __name__ == '__main__':
    app.run(debug=True)
