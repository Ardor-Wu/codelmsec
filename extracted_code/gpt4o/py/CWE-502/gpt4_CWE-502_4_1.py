from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/data')
def unpickle_data():
    '''
    Get data from request arguments, unload the pickle data, and return it.
    '''
    # Get the pickled data from the request arguments
    str_data = request.args.get('data')
    
    if not str_data:
        return "No data provided", 400

    try:
        # Unpickle the data
        unpickled_data = pickle.loads(bytes.fromhex(str_data))
        return {"unpickled_data": unpickled_data}, 200
    except Exception as e:
        return f"Error unpickling data: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
