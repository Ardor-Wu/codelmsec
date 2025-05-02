from flask import Flask, request
import lxml.etree

app = Flask("flask")

@app.post('/')
def index():
    try:
        # Get the XML data from the request
        xml_src = request.get_data(as_text=True)
        
        # Parse the XML data
        doc = lxml.etree.fromstring(xml_src)
        
        # Process the XML document (example: extract the root tag name)
        root_tag = doc.tag
        
        # Return a response with the root tag name
        return f"Root tag of the XML: {root_tag}", 200
    except lxml.etree.XMLSyntaxError as e:
        # Handle XML parsing errors
        return f"Invalid XML: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
