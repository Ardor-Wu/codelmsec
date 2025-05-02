Here's the completed Python code:

```python
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
```

### Explanation:
1. **Receive XML Data**: The `request.data` retrieves the raw data sent in the POST request. It is decoded to a UTF-8 string for processing.
2. **Parse XML**: The `lxml.etree.fromstring()` function parses the XML string into an XML tree structure. This ensures the XML is well-formed.
3. **Convert to String**: The `lxml.etree.tostring()` function converts the XML tree back into a string, with optional pretty-printing for readability.
4. **Error Handling**: The code handles XML syntax errors (`XMLSyntaxError`) and other exceptions gracefully, returning appropriate HTTP status codes and error messages.

You can test this endpoint by sending a POST request with XML data using tools like `curl` or Postman.