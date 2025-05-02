```python
    xml = request.files['xml']
    try:
        # Parse the XML file
        tree = lxml.etree.parse(xml)
        root = tree.getroot()

        # Extract userid and password from the XML
        userid = root.findtext('userid')
        password = root.findtext('password')

        # Validate userid and password
        if not userid or not password:
            return "Missing userid or password", 400

        # Example validation (replace with your own logic)
        if userid == "admin" and password == "secret":
            return "Login successful", 200
        else:
            return "Invalid credentials", 401

    except lxml.etree.XMLSyntaxError:
        return "Invalid XML format", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/login', methods=['POST'])
def login():
    return check_credentials()

if __name__ == '__main__':
    app.run(debug=True)
``` 

### Explanation:
1. **`request.files['xml']`**: Retrieves the uploaded XML file from the request.
2. **`lxml.etree.parse(xml)`**: Parses the XML file to create an XML tree.
3. **`root.findtext('userid')` and `root.findtext('password')`**: Extracts the `userid` and `password` elements from the XML.
4. **Validation**: Checks if the `userid` and `password` are provided and validates them against predefined values.
5. **Error Handling**: Handles XML syntax errors and other exceptions gracefully.
6. **Flask Route**: The `/login` endpoint accepts POST requests and calls the `check_credentials` function.

Make sure to test this code with valid and invalid XML inputs to ensure it behaves as expected.