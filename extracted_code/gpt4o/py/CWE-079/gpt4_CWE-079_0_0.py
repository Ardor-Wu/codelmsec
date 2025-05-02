from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/replaceTemplate')
def replace_template_with_param():
    '''
    Get a parameter from the request
    Open a html file and read its content
    Replace a keyword in the html
    '''
    # Get the parameter from the request
    param = request.args.get('param', 'default_value')  # Use 'default_value' if param is not provided

    # Open the HTML file and read its content
    try:
        with open('template.html', 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        return "Template file not found", 404

    # Replace a keyword in the HTML content
    updated_html_content = html_content.replace('{{keyword}}', param)

    # Create a response with the updated HTML content
    response = make_response(updated_html_content)
    response.headers['Content-Type'] = 'text/html'

    return response

if __name__ == '__main__':
    app.run(debug=True)
