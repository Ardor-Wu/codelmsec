```python
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/xml", methods=["POST"])
def convert_xml_to_string():
    '''
    Parse xml data from request and return xml document as a string
    '''
    try:
        # Get the raw XML data from the request
        xml_src = request.get_data()
        
        # Parse the XML data using lxml
        doc = lxml.etree.fromstring(xml_src)
        
        # Convert the XML document to a string
        xml_string = lxml.etree.tostring(doc, pretty_print=True, encoding="unicode")
        
        return xml_string, 200
    except lxml.etree.XMLSyntaxError as e:
        # Handle XML parsing errors
        return f"Invalid XML: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
```