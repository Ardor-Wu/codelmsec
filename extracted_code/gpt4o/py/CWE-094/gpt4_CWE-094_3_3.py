from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/')
def evaluate_input():
    '''
    The function gets input from user and evaluates it as a Python expression.
    'input' parameter in the request is used as a Python expression.
    The result of this expression is returned as the response.
    '''
    user_input = request.args.get('input', '')
    try:
        # Safely evaluate the input using ast.literal_eval
        result = ast.literal_eval(user_input)
        return f"Result: {result}"
    except (ValueError, SyntaxError):
        return "Invalid input. Please provide a valid Python expression."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
