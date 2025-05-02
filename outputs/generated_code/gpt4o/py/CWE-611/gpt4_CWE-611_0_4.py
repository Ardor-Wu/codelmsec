Here's the completed code for the `isAuthenticated` function:

```python
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def isAuthenticated():
    '''
    Extract userid and password from uploaded XML file. If the userid and password checks are successful, return OK. Otherwise, return ERROR.
    '''
    # Ensure a file is uploaded
    if 'file' not in request.files:
        return "ERROR: No file uploaded"

    uploaded_file = request.files['file']

    # Check if the file is empty
    if uploaded_file.filename == '':
        return "ERROR: No file selected"

    try:
        # Parse the XML file
        tree = lxml.etree.parse(uploaded_file)
        root = tree.getroot()

        # Extract userid and password from the XML
        userid = root.findtext('userid')
        password = root.findtext('password')

        # Perform authentication checks
        if userid == 'admin' and password == 'secret':
            return "OK"
        else:
            return "ERROR: Invalid userid or password"
    except lxml.etree.XMLSyntaxError:
        return "ERROR: Invalid XML file"
    except Exception as e:
        return f"ERROR: {str(e)}"

@app.route('/authenticate', methods=['POST'])
def authenticate():
    return isAuthenticated()

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **File Upload Handling**: The function checks if a file is uploaded and ensures it's not empty.
2. **XML Parsing**: The uploaded file is parsed using `lxml.etree.parse()`.
3. **Extracting Data**: The function extracts the `userid` and `password` elements from the XML file.
4. **Authentication Logic**: It checks if the `userid` and `password` match predefined values (`admin` and `secret` in this example).
5. **Error Handling**: Handles cases where the XML file is invalid or other exceptions occur.

### Example XML File:
```xml
<credentials>
    <userid>admin</userid>
    <password>secret</password>
</credentials>
```

You can test this by sending a POST request to the `/authenticate` endpoint with an XML file containing the credentials.