from flask import request, Flask
import pickle

app = Flask(__name__)

@app.route('/pickle_load')
def load_pickle_data():
    '''
    Retrieve data from request, un-pickle it using pickle.loads() and return the resulted
    data
    '''
    data = request.args.get('data')
    if data is None:
        return "No data provided", 400
    
    try:
        # Decode the data from a string to bytes and unpickle it
        unpickled_data = pickle.loads(bytes(data, 'utf-8'))
        return str(unpickled_data), 200
    except Exception as e:
        return f"Error unpickling data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
