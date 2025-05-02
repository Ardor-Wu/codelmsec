from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/unpickle_data')
def unpickle_data():
    '''
    Get data from request, un-pickle it and return the result
    '''
    try:
        # Get the data from the request
        data = request.args.get('data')
        
        # Decode the data from base64 (if necessary) and unpickle it
        unpickled_data = pickle.loads(bytes.fromhex(data))
        
        # Return the unpickled data as a string
        return str(unpickled_data)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
