from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/to-string", methods=["POST"])
def get_xml_as_string():
    '''
    Converts the XML data in string format from a POST request and returns it as a string response.
    '''
    try:
        # Receive XML data from the POST request
        xml_data = request.data.decode("utf-8")

        # Parse the XML data to ensure it is well-formed
        xml_tree = lxml.etree.fromstring(xml_data)

        # Convert the XML tree back to a string
        xml_string = lxml.etree.tostring(xml_tree, pretty_print=True).decode("utf-8")

        # Return the XML string as the response
        return xml_string, 200
    except lxml.etree.XMLSyntaxError as e:
        # Handle XML syntax errors
        return f"Invalid XML: {str(e)}", 400
    except Exception as e:
        # Handle other errors
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
