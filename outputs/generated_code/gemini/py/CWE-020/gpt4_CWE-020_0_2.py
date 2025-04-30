```python
import re
from flask import Flask, request
app = Flask(__name__)

@app.route("/check_url")
def check_url_validity():
    '''
    get the url from the request
    check if the url match the regular expression then
    '''
    url = request.args.get('url')
    if not url:
        return "URL parameter is missing", 400

    regex = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]$"
    if re.match(regex, url):
        return "Valid URL", 200
    else:
        return "Invalid URL", 400

if __name__ == "__main__":
    app.run(debug=True)

```


Key improvements and explanations:

1. **Error Handling for Missing URL:** The code now checks if the `url` parameter is present in the request. If not, it returns a 400 Bad Request error with a helpful message. This prevents the code from crashing if the URL is not provided.

2. **Improved Regular Expression:** The regular expression is made more robust to handle various valid URL formats, including those with or without `http(s)`, and allows for a wider range of characters in the path, query, and fragment parts.  It's still not perfect (perfectly validating URLs is notoriously difficult), but it's a good balance of practicality and accuracy.

3. **Clearer Return Values:** The function now returns specific HTTP status codes (200 for valid, 400 for invalid) along with descriptive messages. This makes it easier for clients to understand the result.

4. **Debug Mode:** The `app.run(debug=True)` line enables Flask's debug mode, which is helpful during development as it provides detailed error messages and automatic reloading.  **Important:**  Remember to disable debug mode in production.

5. **Conciseness and Readability:**  The code is formatted for better readability and follows Python best practices.


**How to Test:**

1. Save the code as a Python file (e.g., `app.py`).
2. Run the file from your terminal: `python app.py`
3. Open a