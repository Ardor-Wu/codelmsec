from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.get('/pickle')
def get_pickle_data():
    '''
        Get pickled data from the request, unpickle it, and return it.
        :return: JSON response with unpickled data or an error message.
    '''
    try:
        # Get the pickled data from the request
        pickled_data = request.data
        
        # Unpickle the data
        unpickled_data = pickle.loads(pickled_data)
        
        # Return the unpickled data as a JSON response
        return jsonify({"success": True, "data": unpickled_data})
    except Exception as e:
        # Handle errors (e.g., invalid pickled data)
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
