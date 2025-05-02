user_input = request.args.get('input', '')  # Get the user input from query parameters
    try:
        # Evaluate the user input as a Python expression
        evaluated_result = eval(user_input)
        return str(evaluated_result)  # Return the evaluated result as a string
    except Exception as e:
        # Handle any errors that occur during evaluation
        return f"Error: {str(e)}"
