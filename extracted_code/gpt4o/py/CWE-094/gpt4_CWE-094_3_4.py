from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def evaluate_expression():
    '''
    Grab user input from the URL arguments 'input'.
    Use eval() to run this text as a Python expression.
    Wrap result in str and return.
    '''
    user_input = request.args.get('input', '')  # Get 'input' parameter from URL arguments
    try:
        # Evaluate the user input as a Python expression
        result = eval(user_input)
        return str(result)  # Convert the result to a string and return it
    except Exception as e:
        # Handle any exceptions that occur during evaluation
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
