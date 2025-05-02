# the URL is stored as a variable called "url"
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Perform some action with the URL if needed
            print(f"URL received: {url}")
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve the URL from the form submission
        url = request.form.get("url")
        if url:
            # Redirect to the after_request logic
            return redirect(url)
    return '''
        <form method="post">
            <label for="url">Enter URL:</label>
            <input type="text" id="url" name="url">
            <button type="submit">Submit</button>
        </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
