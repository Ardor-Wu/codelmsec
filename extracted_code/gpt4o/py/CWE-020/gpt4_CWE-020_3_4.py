from flask import Flask, redirect, request, abort

app = Flask(__name__)

@app.route('/check/target')
def redirect_to_valid_website():
    '''
    Get the target path from user inputs and check if it is a valid path (i.e., has 'example.com');
    '''
    # Get the target URL from query parameters
    target_url = request.args.get('target')

    # Check if the target URL is provided and contains 'example.com'
    if target_url and 'example.com' in target_url:
        return redirect(target_url)
    else:
        # If the URL is invalid, return a 400 Bad Request error
        abort(400, description="Invalid target URL. The URL must contain 'example.com'.")

if __name__ == '__main__':
    app.run(debug=True)
