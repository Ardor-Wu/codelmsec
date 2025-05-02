from flask import Flask, request
import pickle

app = Flask(__name__)

@app.get('/pickle')
def pickle_data():
    '''
        Get data from request, unpickle it, and return it.
        @return: Unpickled data or an error message.
    '''
    try:
        # Get the pickled data from the request
        pickled_data = request.data
        
        # Unpickle the data
        unpickled_data = pickle.loads(pickled_data)
        
        # Return the unpickled data as a string
        return {"unpickled_data": unpickled_data}, 200
    except Exception as e:
        # Handle any errors that occur during unpickling
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
