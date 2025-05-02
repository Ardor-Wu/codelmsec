from flask import Flask, request
import lxml.etree

app = Flask('app')

@app.route("/user", methods=["POST"])
def user():
    '''
    1. Get the XML from the request
    2. Parse the XML
    '''
    try:
        # Step 1: Get the XML from the request
        xml_data = request.data  # Retrieve raw XML data from the request body

        # Step 2: Parse the XML
        parser = lxml.etree.XMLParser(recover=True)  # Create an XML parser
        xml_tree = lxml.etree.fromstring(xml_data, parser)  # Parse the XML data into an ElementTree

        # Example: Extract a specific element (optional, based on your XML structure)
        # Assuming the XML has a structure like <user><name>John</name></user>
        user_name = xml_tree.findtext('name')  # Extract the 'name' element text
        if user_name:
            return f"User name: {user_name}", 200
        else:
            return "Name element not found in XML", 400

    except lxml.etree.XMLSyntaxError as e:
        return f"Invalid XML: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
