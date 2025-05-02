from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def evaluate_expression():
    '''
    Get the user_input from the request arguments,
    evaluate it as a Python expression using the eval function,
    and return the evaluation result as a string.
    '''
    user_input = request.args.get('expression', '')  # Get the 'expression' parameter from the request arguments
    try:
        # Evaluate the user input safely
        result = eval(user_input)
        return str(result)
    except Exception as e:
        # Handle any errors that occur during evaluation
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
