```python
    3. validate it against an XML schema (if provided)
    4. return a response based on the validation result
    '''
    # Step 1: Get the XML from the request
    xml_data = request.data

    try:
        # Step 2: Parse the XML
        xml_tree = lxml.etree.fromstring(xml_data)

        # Optional Step 3: Validate against an XML schema (if you have one)
        # Uncomment and provide the schema if needed
        # schema_root = lxml.etree.XML('''<your XML schema here>''')
        # schema = lxml.etree.XMLSchema(schema_root)
        # if not schema.validate(xml_tree):
        #     return "Invalid XML according to schema", 400

        # If parsing and validation succeed
        return "XML is valid and well-formed", 200

    except lxml.etree.XMLSyntaxError as e:
        # Handle XML syntax errors
        return f"Invalid XML: {str(e)}", 400

    except Exception as e:
        # Handle other unexpected errors
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```