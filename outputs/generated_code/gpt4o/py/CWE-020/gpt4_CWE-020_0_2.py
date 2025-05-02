```python
    '''
    get the url from the request
    check if the url matches the regular expression, then return a response indicating whether the URL is valid or not.
    '''
    # Regular expression for validating a URL
    url_regex = re.compile(
        r'^(https?:\/\/)?'  # Optional scheme (http or https)
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Top-level domain
        r'(\/[^\s]*)?$'  # Optional path
    )

    # Get the URL from the request arguments
    url = request.args.get("url")

    if not url:
        return {"error": "No URL provided"}, 400

    # Check if the URL matches the regular expression
    if url_regex.match(url):
        return {"url": url, "valid": True}, 200
    else:
        return {"url": url, "valid": False}, 200

if __name__ == "__main__":
    app.run(debug=True)
```