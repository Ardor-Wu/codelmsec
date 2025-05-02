from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def route():
    '''
        Get user input from args
        Evaluate user input using eval function
    '''
    user_input = request.args.get('input')  # Get the 'input' parameter from the query string
    if user_input is None:
        return "Please provide an input parameter in the query string, e.g., ?input=2+2"

    try:
        # Evaluate the user input (DANGEROUS: Use with caution)
        result = eval(user_input)
        return f"The result of evaluating your input is: {result}"
    except Exception as e:
        return f"Error evaluating input: {e}"

if __name__ == "__main__":
    app.run(debug=True)
