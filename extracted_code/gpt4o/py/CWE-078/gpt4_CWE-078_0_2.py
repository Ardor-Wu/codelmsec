from flask import Flask, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping_specified_url():
    '''
    Receive 'url' from the GET request and ping it,
    then redirect to the same URL.
    '''
    # Obtain the 'url' parameter from the GET request
    url = request.args.get('url')
    
    if not url:
        return "Error: 'url' parameter is required.", 400

    try:
        # Ping the specified URL
        result = subprocess.run(
            ['ping', '-c', '4', url],  # '-c 4' sends 4 ping requests
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Log the ping result (optional)
        print(result.stdout)
        print(result.stderr)

        # Check if the ping was successful
        if result.returncode == 0:
            return redirect(url)
        else:
            return f"Ping failed for URL: {url}. Error: {result.stderr}", 500
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
