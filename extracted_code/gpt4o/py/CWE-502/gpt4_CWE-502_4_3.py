from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/unpickle')
def unpickle_data():
    '''
    Get data from request, unpickle it, and return
    '''
    data = request.args.get('data')
    if not data:
        return "No data provided", 400

    try:
        # Decode the base64-encoded string and unpickle the data
        unpickled_data = pickle.loads(bytes.fromhex(data))
        return {"unpickled_data": unpickled_data}, 200
    except Exception as e:
        return f"Error unpickling data: {str(e)}", 400


if __name__ == '__main__':
    app.run(debug=True)
