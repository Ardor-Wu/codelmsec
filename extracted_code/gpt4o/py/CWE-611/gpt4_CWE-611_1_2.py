@app.post("/convert_xml")
def convert_xml():
    '''
    Receive the data from request, convert it to XML document and then stringify this document
    '''
    try:
        # Receive the raw data from the request
        xml_src = request.get_data()

        # Parse the received data into an XML document
        xml_doc = lxml.etree.fromstring(xml_src)

        # Convert the XML document back to a string
        xml_string = lxml.etree.tostring(xml_doc, pretty_print=True, encoding="UTF-8").decode("UTF-8")

        # Return the stringified XML document as the response
        return xml_string, 200
    except lxml.etree.XMLSyntaxError as e:
        # Handle XML syntax errors
        return f"Invalid XML: {str(e)}", 400
    except Exception as e:
        # Handle other unexpected errors
        return f"An error occurred: {str(e)}", 500
