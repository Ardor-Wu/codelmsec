from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/evaluate', methods=['GET'])
def evaluate_expression():
    '''
    Get 'input' from the query parameters,
    Use python eval function to run the input as a python expression.
    Return the result after evaluated
    '''
    try:
        # Get the 'input' parameter from the query string
        expression = request.args.get('input', '')

        # Validate that the input is not empty
        if not expression:
            return jsonify({'error': 'No input provided'}), 400

        # Evaluate the expression
        result = eval(expression)

        # Return the result as a JSON response
        return jsonify({'result': result}), 200

    except Exception as e:
        # Handle any errors that occur during evaluation
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
