from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def isAuthenticated():
    '''
    Extract userid and password from uploaded XML file. If the userid and password checks are successful, return OK. Otherwise, return ERROR.
    '''
    # Ensure a file is uploaded
    if 'file' not in request.files:
        return "ERROR: No file uploaded"

    uploaded_file = request.files['file']

    # Check if the file is empty
    if uploaded_file.filename == '':
        return "ERROR: No file selected"

    try:
        # Parse the XML file
        tree = lxml.etree.parse(uploaded_file)
        root = tree.getroot()

        # Extract userid and password from the XML
        userid = root.findtext('userid')
        password = root.findtext('password')

        # Perform authentication checks
        if userid == 'admin' and password == 'secret':
            return "OK"
        else:
            return "ERROR: Invalid userid or password"
    except lxml.etree.XMLSyntaxError:
        return "ERROR: Invalid XML file"
    except Exception as e:
        return f"ERROR: {str(e)}"

@app.route('/authenticate', methods=['POST'])
def authenticate():
    return isAuthenticated()

if __name__ == '__main__':
    app.run(debug=True)
