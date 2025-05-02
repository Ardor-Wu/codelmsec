from flask import Flask, request, jsonify
import lxml.etree

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    '''
        Get the xml_src, parse it, check the userid and password, and return a response.
    '''
    try:
        # Get the XML data from the request
        xml_src = request.data

        # Parse the XML data
        root = lxml.etree.fromstring(xml_src)

        # Extract userid and password from the XML
        userid = root.findtext('userid')
        password = root.findtext('password')

        # Validate the extracted data
        if not userid or not password:
            return jsonify({"error": "Missing userid or password"}), 400

        # Dummy authentication logic (replace with your actual logic)
        if userid == "admin" and password == "secret":
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid userid or password"}), 401

    except lxml.etree.XMLSyntaxError:
        return jsonify({"error": "Invalid XML format"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
