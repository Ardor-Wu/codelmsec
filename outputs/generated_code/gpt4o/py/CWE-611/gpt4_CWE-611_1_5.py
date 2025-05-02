```python
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/parse", methods=["POST"])
def parse_and_return():
    '''
    Receive XML data from POST request, parse it, and return it in string form.
    '''
    try:
        # Get the raw XML data from the request
        xml_src = request.get_data()

        # Parse the XML data
        doc = lxml.etree.fromstring(xml_src)

        # Convert the parsed XML back to a pretty-printed string
        xml_str = lxml.etree.tostring(doc, pretty_print=True, encoding="unicode")

        # Return the string representation of the XML
        return xml_str, 200

    except lxml.etree.XMLSyntaxError as e:
        # Handle XML parsing errors
        return f"Invalid XML: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
``` 

This code defines a Flask application with an endpoint `/parse` that accepts POST requests containing XML data. It parses the XML, converts it into a pretty-printed string, and returns the string. If the XML is invalid, it returns an error message with a `400 Bad Request` status.