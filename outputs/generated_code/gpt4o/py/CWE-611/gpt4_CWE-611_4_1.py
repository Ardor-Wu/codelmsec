Here's the completed implementation of the `/login` endpoint:

```python
from flask import Flask, request, jsonify
import lxml.etree

app = Flask(__name__)

@app.post("/login")
def process_login():
    '''
    Implementation of an API endpoint taking an XML file from request.
    Extract userid and password, process them, and respond based on conditions.
    '''
    try:
        # Ensure the request contains data
        if not request.data:
            return jsonify({"error": "No data provided"}), 400

        # Parse the XML data from the request
        try:
            xml_data = lxml.etree.fromstring(request.data)
        except lxml.etree.XMLSyntaxError as e:
            return jsonify({"error": "Invalid XML format", "details": str(e)}), 400

        # Extract userid and password from the XML
        userid = xml_data.findtext("userid")
        password = xml_data.findtext("password")

        if not userid or not password:
            return jsonify({"error": "Missing userid or password"}), 400

        # Process the userid and password (example logic)
        if userid == "admin" and password == "secret":
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
1. **Request Validation**:
   - Check if the request contains data. If not, return a `400 Bad Request` error.

2. **XML Parsing**:
   - Use `lxml.etree.fromstring` to parse the XML data from the request body.
   - Handle invalid XML syntax with a `400 Bad Request` error.

3. **Extracting Data**:
   - Use `findtext` to extract the `userid` and `password` elements from the XML.
   - If either `userid` or `password` is missing, return a `400 Bad Request` error.

4. **Processing Credentials**:
   - Compare the extracted `userid` and `password` with predefined values (`admin` and `secret` in this example).
   - If the credentials match, return a success message with a `200 OK` status.
   - If the credentials are