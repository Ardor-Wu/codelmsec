from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_evaluated_input():
    '''
    Getting 'input' parameter from the GET request and evaluating it as a Python expression.
    Returning string representation of that result.
    '''
    user_input = request.args.get('input', '')  # Get 'input' parameter from the query string
    try:
        # WARNING: Using eval is dangerous and should be avoided with untrusted input!
        result = eval(user_input)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
