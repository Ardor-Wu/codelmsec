from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def evaluate_input():
    '''
    Get 'input' from the request arguments.
    Run it as a Python expression and return the evaluated result as a string.
    '''
    user_input = request.args.get('input', '')  # Safely get 'input' from request arguments
    try:
        result = eval(user_input)  # Evaluate the user input (DANGEROUS!)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)


from sympy import sympify

   @app.route('/')
   def evaluate_input():
       user_input = request.args.get('input', '')
       try:
           result = sympify(user_input)  # Safely evaluate mathematical expressions
           return str(result)
       except Exception as e:
           return f"Error: {str(e)}"
