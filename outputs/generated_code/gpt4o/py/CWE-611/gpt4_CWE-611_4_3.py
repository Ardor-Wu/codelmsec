```python
@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to handle user login. Expects XML data with 'userid' and 'password' fields.
    """
    try:
        # Parse the incoming XML data
        xml_data = request.data
        root = lxml.etree.fromstring(xml_data)

        # Extract 'userid' and 'password' from the XML
        userid = root.findtext('userid')
        password = root.findtext('password')

        if not userid or not password:
            return "Missing 'userid' or 'password' in the request.", 400

        # Validate the credentials
        if checkPassword(userid, password):
            return "Login successful!", 200
        else:
            return "Invalid credentials.", 401

    except lxml.etree.XMLSyntaxError:
        return "Invalid XML format.", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
``` 

This code defines a `/login` endpoint that accepts POST requests with XML data containing `userid` and `password`. It parses the XML, validates the credentials using the `checkPassword` function, and returns appropriate responses. Note that the `checkPassword` function is a placeholder and should be implemented with actual authentication logic.