'''
    parse the xml file from the request, find the userid and the username, and return them in a JSON response.
    '''
    try:
        # Get the uploaded file from the request
        uploaded_file = request.files['file']
        
        # Parse the XML file
        tree = lxml.etree.parse(uploaded_file)
        root = tree.getroot()
        
        # Extract userid and username from the XML
        userid = root.findtext('userid')
        username = root.findtext('username')
        
        # Check if both userid and username exist
        if userid is None or username is None:
            return {"error": "Missing userid or username in the XML file"}, 400
        
        # Return the extracted data in JSON format
        return {"userid": userid, "username": username}, 200
    
    except Exception as e:
        # Handle errors (e.g., invalid XML file)
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
