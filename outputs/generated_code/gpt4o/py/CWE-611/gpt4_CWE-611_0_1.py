```python
from flask import Flask, request, jsonify
import lxml.etree

app = Flask(__name__)

def checkPassword(user_id, password):
    # Replace this with your actual password-checking logic
    # For example, you might query a database to validate the credentials
    if user_id == "admin" and password == "password123":
        return True
    return False

@app.route('/login', methods=['POST'])
def login_with_xml():
    '''
    Accepts an XML file from a client via POST, gets the user ID and password values from the XML,
    then calls checkPassword to validate the credentials.
    '''
    try:
        # Ensure the request contains data
        if not request.data:
            return jsonify({"error": "No data provided"}), 400

        # Parse the XML data from the request
        xml_data = lxml.etree.fromstring(request.data)

        # Extract user ID and password from the XML
        user_id = xml_data.findtext('user_id')
        password = xml_data.findtext('password')

        # Validate that both user_id and password are present
        if not user_id or not password:
            return jsonify({"error": "Missing user_id or password in the XML"}), 400

        # Check the credentials using the checkPassword function
        if checkPassword(user_id, password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except lxml.etree.XMLSyntaxError:
        return jsonify({"error": "Invalid XML format"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
1. **`checkPassword` Function**:
   - This function is a placeholder for the actual logic to validate user credentials. Replace it with your own implementation, such as querying a database.

2. **XML Parsing**:
   - The `lxml.etree.fromstring` function is used to parse the XML data from the request body.
   - The `findtext` method retrieves the text content of specific XML elements (`user_id` and `password`).

3. **Error Handling**:
   - If the XML is malformed, an `XMLSyntaxError` is caught and an appropriate error message is returned.
  