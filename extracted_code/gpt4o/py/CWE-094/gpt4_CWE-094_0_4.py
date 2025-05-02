from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def compute():
    '''
    Get the 'input' from request arguments,
    evaluate the user_input string as a Python expression,
    and return the result as a string.
    '''
    user_input = request.args.get('input')
    try:
        # Evaluate the user_input string as a Python expression
        result = eval(user_input)
        return str(result)
    except Exception as e:
        # Handle errors gracefully
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
