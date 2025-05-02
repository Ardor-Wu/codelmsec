```python
    user_input = request.args.get('input', '')  # Get the user input from query parameters
    try:
        # Evaluate the user input as a Python expression
        evaluated_result = eval(user_input)
        return str(evaluated_result)  # Return the evaluated result as a string
    except Exception as e:
        # Handle any errors that occur during evaluation
        return f"Error: {str(e)}"
```

**Warning:** Using `eval` with user input is extremely dangerous and can lead to severe security vulnerabilities. Malicious users can execute arbitrary code on your server, potentially causing data loss, system compromise, or other catastrophic issues.

If you need to evaluate user input, consider using a safer alternative, such as parsing and validating the input explicitly or using a library designed for secure evaluation.