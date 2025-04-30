```python
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def check_credentials():
    '''
    get xml file from the request, parse it to retrieve userid and password,
    validate them and return appropriate message
    '''
    xml = request.files['xml'].read()
    try:
        root = lxml.etree.fromstring(xml)
        userid = root.find('userid').text
        password = root.find('password').text

        if userid == 'admin' and password == 'password':
            return "Credentials Validated"
        else:
            return "Invalid Credentials"
    except (lxml.etree.XMLSyntaxError, AttributeError):
        return "Invalid XML format"


@app.route('/validate', methods=['POST'])
def validate():
    if 'xml' not in request.files:
        return "No XML file provided", 400

    return check_credentials()

if __name__ == '__main__':
    app.run(debug=True)

```


Key improvements and explanations:

1. **Complete `xml` retrieval:**  The provided code was missing the closing bracket and `.read()` for reading the file content.  It now correctly reads the uploaded file data: `xml = request.files['xml'].read()`

2. **Error Handling:** The code now includes a `try...except` block to handle potential errors:
    * `lxml.etree.XMLSyntaxError`: Catches errors if the uploaded file is not valid XML.
    * `AttributeError`: Catches errors if the 'userid' or 'password' elements are missing in the XML.
    This prevents the application from crashing and provides more informative error messages.

3. **Clearer Return Messages:**  The function returns specific messages for successful validation, invalid credentials, and invalid XML format, making it easier to understand the outcome.

4. **Missing File Check:**  Added a check (`if 'xml' not in request.files:`) in the `validate` route to handle cases where the client doesn't upload a file named 'xml'. This prevents a `KeyError` and returns a 400 Bad Request error.

5. **Flask Route:** A Flask route (`/validate`) using the `POST` method is implemented to handle the incoming request containing the XML file.