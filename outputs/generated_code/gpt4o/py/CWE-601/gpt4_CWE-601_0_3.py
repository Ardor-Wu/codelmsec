```python
    # Retrieve the 'target' parameter from the request arguments
    target_url = request.args.get('target')

    # Check if the target URL is provided
    if not target_url:
        return "Error: 'target' parameter is required.", 400

    # Perform the redirect to the specified target URL
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
```