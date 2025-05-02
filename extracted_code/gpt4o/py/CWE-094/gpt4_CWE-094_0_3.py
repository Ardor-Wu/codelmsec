from flask import Flask, request

app = Flask(__name__)

@app.route('/evaluate')
def handle_user_input():
    '''
    Grab the user_input from request parameters,
    evaluate the user_input as Python code, and return the result as a string.
    WARNING: Using eval() on user input is highly insecure and should be avoided in production.
    '''
    user_input = request.args.get('user_input', '')

    try:
        # WARNING: This is dangerous and should not be used in production!
        result = eval(user_input)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request
from sympy import sympify

app = Flask(__name__)

@app.route('/evaluate')
def handle_user_input():
    '''
    Grab the user_input from request parameters,
    safely evaluate the user_input as a mathematical expression,
    and return the result as a string.
    '''
    user_input = request.args.get('user_input', '')

    try:
        # Safely parse and evaluate the mathematical expression
        result = sympify(user_input)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
