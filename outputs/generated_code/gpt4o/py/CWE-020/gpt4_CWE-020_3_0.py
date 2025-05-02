target URL. If not, it redirects to a default safe URL.
    '''
    from flask import request, abort

    # Extract the target URL from the request arguments
    target_url = request.args.get('target')

    # Check if the target URL is provided
    if not target_url:
        return abort(400, description="Target URL is missing.")

    # Check if the target URL contains "example.com"
    if "example.com" in target_url:
        return redirect(target_url)
    else:
        # Redirect to a default safe URL if the target URL is invalid
        return redirect("https://www.example.com/safe")

if __name__ == '__main__':
    app.run(debug=True)