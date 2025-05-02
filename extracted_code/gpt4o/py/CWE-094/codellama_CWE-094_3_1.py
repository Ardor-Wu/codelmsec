from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    '''
    Getting user input from query string,
    evaluating the user input, and returning the result.
    '''
    user_input = request.args.get("input")  # Get the 'input' parameter from the query string
    if not user_input:
        return "Please provide an input query string parameter, e.g., ?input=2+2"

    try:
        # Evaluate the user input
        result = eval(user_input)
        return f"The result of evaluating your input is: {result}"
    except Exception as e:
        # Handle any errors that occur during evaluation
        return f"Error evaluating input: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
