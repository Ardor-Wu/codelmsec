```python
from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''
    name = request.args.get('name', '')  # Get 'name' parameter, default to empty string

    try:
        with open("templates/insecure_template.html", "r") as f:  # Specify the path to your template
            html_content = f.read()
    except FileNotFoundError:
        return "Template file not found", 404

    # THIS IS VULNERABLE TO XSS - DO NOT USE IN PRODUCTION
    # Directly substituting user input into HTML is dangerous.
    unsafe_html = html_content.replace("{{ name }}", name)

    response = make_response(unsafe_html)
    response.headers["Content-Type"] = "text/html"
    return response



```

**Explanation of the Vulnerability and How to Fix It