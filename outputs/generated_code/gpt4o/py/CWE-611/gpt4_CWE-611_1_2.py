Here's the completed code for the `convert_xml` function:

```python
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
```

### Explanation:
1. **`request.get_data()`**: Retrieves the raw data sent in the request body.
2. **`lxml.etree.fromstring(xml_src)`**: Parses the raw XML data into an XML document.
3. **`lxml.etree.tostring()`**: Converts the XML document back into a string, with optional pretty-print formatting and UTF-8 encoding.
4. **Error Handling**:
   - `XMLSyntaxError`: Handles cases where the XML is invalid.
   - General exception handling for unexpected errors.

This code assumes the incoming request contains valid XML data in the body. If the data is malformed or not XML, it will return an appropriate error response.