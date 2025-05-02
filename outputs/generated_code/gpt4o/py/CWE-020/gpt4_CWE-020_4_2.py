specific pattern (e.g., starts with "http://" or "https://", followed by a domain name and optional path). Return a response indicating whether the URL is valid or not.
    '''
    url = request.args.get("url")
    if not url:
        return {"error": "No URL provided"}, 400

    # Regular expression to validate the URL
    url_pattern = re.compile(
        r'^(https?://)'  # Match "http://" or "https://"
        r'([a-zA-Z0-9.-]+)'  # Match domain name (letters, numbers, dots, hyphens)
        r'(:[0-9]+)?'  # Optional port number
        r'(/.*)?$'  # Optional path
    )

    if url_pattern.match(url):
        return {"message": "Valid URL"}, 200
    else:
        return {"message": "Invalid URL"}, 400


if __name__ == "__main__":
    app.run(debug=True)