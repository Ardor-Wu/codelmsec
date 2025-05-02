Here is the completed Python code for the `ping` function:

```python
@app.route("/", methods=["POST"])
def ping():
    '''
    Receive a URL from a POST request and ping it.
    '''
    # Get the URL from the POST request
    data = request.get_json()
    if not data or 'url' not in data:
        return {"error": "Missing 'url' in request body"}, 400

    url = data['url']

    # Validate the URL
    if not isinstance(url, str) or not url:
        return {"error": "Invalid URL"}, 400

    try:
        # Use the subprocess module to ping the URL
        response = subprocess.run(
            ["ping", "-c", "4", url],  # Ping the URL 4 times
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the ping was successful
        if response.returncode == 0:
            return {"message": "Ping successful", "output": response.stdout}, 200
        else:
            return {"message": "Ping failed", "error": response.stderr}, 400

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    # Run the Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

### Explanation:
1. **Route Definition**: The `ping` function is defined as the handler for the root (`"/"`) route, and it accepts only `POST` requests.
2. **Input Validation**: The function expects a JSON payload with a key `url`. If the key is missing or invalid, it returns an error response.
3. **Ping Command**: The `subprocess.run` function is used to execute the `ping` command. The `-c 4` flag specifies that the ping should be sent 4 times.
4. **Error Handling**: The function checks the return code of the `ping` command to determine if it was successful. If an exception occurs during execution, it is caught and returned as an error response.
5. **Flask App Execution**: The app runs on port 5000 by default, but this can be overridden by setting the `PORT` environment variable.

### Note:
- This implementation assumes the server has access to the `ping` command