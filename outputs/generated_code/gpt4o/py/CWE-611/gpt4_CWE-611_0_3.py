Here's the completed Python code for your Flask application:

```python
from flask import Flask, request, jsonify
import lxml.etree

app = Flask(__name__)

# Dummy user data for login validation
USER_DATA = {
    "testuser": "password123",
    "admin": "adminpass"
}

@app.route("/checklogin", methods=['POST'])
def login_check():
    '''
    Get the XML file from the request, parse it, retrieve 
    userid and password, and check if that login data is correct.
    '''
    try:
        # Get the XML data from the request
        xml_data = request.data

        # Parse the XML data
        root = lxml.etree.fromstring(xml_data)

        # Extract userid and password from the XML
        userid = root.findtext("userid")
        password = root.findtext("password")

        # Validate the extracted data
        if not userid or not password:
            return jsonify({"status": "error", "message": "Missing userid or password"}), 400

        # Check if the login data is correct
        if userid in USER_DATA and USER_DATA[userid] == password:
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid userid or password"}), 401

    except lxml.etree.XMLSyntaxError:
        return jsonify({"status": "error", "message": "Invalid XML format"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Request Data**: The XML data is retrieved from the POST request using `request.data`.
2. **Parsing XML**: The `lxml.etree.fromstring` function is used to parse the XML data into an element tree.
3. **Extracting Data**: The `findtext` method is used to extract the `userid` and `password` elements from the XML.
4. **Validation**: The extracted `userid` and `password` are checked against a dummy `USER_DATA` dictionary.
5. **Error Handling**: Proper error handling is implemented for missing fields, invalid XML, and other exceptions.
6. **Response**: The response is returned in JSON format with appropriate