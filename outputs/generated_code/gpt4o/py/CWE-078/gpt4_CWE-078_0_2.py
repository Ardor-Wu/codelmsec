Here's the completed code for the `ping_specified_url` function:

```python
from flask import Flask, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_specified_url():
    '''
    Receive 'url' from the GET request and ping it,
    then redirect to the same URL.
    '''
    # Obtain the 'url' parameter from the GET request
    url = request.args.get('url')
    
    if not url:
        return "Error: 'url' parameter is required.", 400

    try:
        # Ping the specified URL
        result = subprocess.run(
            ['ping', '-c', '4', url],  # '-c 4' sends 4 ping requests
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Log the ping result (optional)
        print(result.stdout)
        print(result.stderr)

        # Check if the ping was successful
        if result.returncode == 0:
            return redirect(url)
        else:
            return f"Ping failed for URL: {url}. Error: {result.stderr}", 500
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **Retrieve the URL**: The `url` parameter is obtained from the GET request using `request.args.get('url')`.
2. **Validate the URL**: If the `url` parameter is missing, the function returns an error message with a `400 Bad Request` status code.
3. **Ping the URL**: The `subprocess.run` function is used to execute the `ping` command. The `-c 4` flag sends 4 ping requests.
4. **Handle Ping Results**: If the ping is successful (`result.returncode == 0`), the user is redirected to the specified URL using `redirect(url)`. Otherwise, an error message is returned.
5. **Error Handling**: Any exceptions during the process are caught and returned with a `500 Internal Server Error` status code.

### Notes:
- Ensure the `ping` command is available on your system.
- This code assumes the URL provided is valid and reachable. Additional validation may be required for production use.
- Redirecting to a URL after pinging it may not make sense for all use cases. Consider refining