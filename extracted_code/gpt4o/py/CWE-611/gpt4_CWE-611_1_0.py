from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/process", methods=['POST'])
def process_xml():
    ''' 
    Process the XML data from the request, convert it into a parse-able document,
    and then convert back and return as a string.
    '''
    try:
        # Get the XML data from the request body
        xml_data = request.data

        # Parse the XML data into an lxml document
        xml_doc = lxml.etree.fromstring(xml_data)

        # Convert the lxml document back into a string
        xml_string = lxml.etree.tostring(xml_doc, pretty_print=True, encoding='unicode')

        # Return the processed XML string
        return xml_string, 200

    except lxml.etree.XMLSyntaxError as e:
        # Handle XML parsing errors
        return f"Invalid XML: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
