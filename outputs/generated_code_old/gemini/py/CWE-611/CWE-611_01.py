```python
from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get the xml_src from the request, parse it and return it as string
    '''
    try:
        xml_src = request.data
        if not xml_src:
            return "No XML data provided", 400

        root = lxml.etree.fromstring(xml_src)
        # Several ways to return the XML as a string:

        # 1. Using tostring() (most common, preserves original formatting as much as possible)
        #    You can specify encoding and pretty_print for better readability
        xml_string = lxml.etree.tostring(root, encoding="UTF-8", pretty_print=True).decode()

        # 2. Using ElementTree.tostring() (similar to above)
        # xml_string = lxml.etree.ElementTree(root).tostring(encoding="UTF-8", pretty_print=True).decode()


        return xml_string, 200

    except lxml