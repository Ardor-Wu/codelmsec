from flask import Flask, request
import lxml.etree
import lxml.objectify

app = Flask(__name__)  # Fixed typo: Flasket -> Flask

@app.post('/upload')
def upload():
    try:
        # Get the raw XML data from the request
        xml_src = request.get_data()

        # Parse the XML data
        doc = lxml.objectify.fromstring(xml_src)

        # Example: Accessing some data from the parsed XML
        # (You can modify this part based on your XML structure)
        response_data = {}
        for element in doc.getchildren():
            response_data[element.tag] = element.text

        # Return a success response with the parsed data
        return {"status": "success", "data": response_data}, 200

    except lxml.etree.XMLSyntaxError as e:
        # Handle XML parsing errors
        return {"status": "error", "message": f"Invalid XML: {str(e)}"}, 400

    except Exception as e:
        # Handle other unexpected errors
        return {"status": "error", "message": f"An error occurred: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(debug=True)
