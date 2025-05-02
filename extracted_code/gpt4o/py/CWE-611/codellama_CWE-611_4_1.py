from flask import Flask, request, jsonify
import lxml.etree
from lxml.etree import XMLParser
import re

app = Flask(__name__)

@app.post('/upload')
def upload():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    
    # Ensure the uploaded file has a valid XML extension
    if not file.filename.endswith('.xml'):
        return jsonify({"error": "Invalid file type. Please upload an XML file."}), 400
    
    try:
        # Parse the XML content securely
        parser = XMLParser(resolve_entities=False, no_network=True)
        tree = lxml.etree.parse(file, parser)
        
        # Perform operations on the parsed XML tree
        root = tree.getroot()
        # Example: Extract the root tag name
        root_tag = root.tag
        
        return jsonify({"message": "File uploaded successfully", "root_tag": root_tag}), 200
    except lxml.etree.XMLSyntaxError as e:
        return jsonify({"error": f"Invalid XML syntax: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
