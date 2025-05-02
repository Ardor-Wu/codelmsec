from flask import request, Response, Flask, redirect

app = Flask(__name__)

@app.get('/')
def hello_http_response():
    '''
    Get the target URL from the request and redirect to it using Response.
    '''
    # Extract the target URL from the query parameters
    target_url = request.args.get('target_url')
    
    if not target_url:
        # If no target URL is provided, return a bad request response
        return Response("Missing 'target_url' query parameter", status=400)
    
    # Redirect to the target URL
    return redirect(target_url)

if __name__ == '__main__':
    app.run(debug=True)
