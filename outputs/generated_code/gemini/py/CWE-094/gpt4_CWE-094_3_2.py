```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def evaluate_expression():
    '''
    get the user_input from the request arguments
    evaluate it as python expression using eval function,
    lastly, return the evaluation result as string
    '''
    try:
        user_input = request.args.get('user_input')
        if user_input is None:
            return "No 'user_input' parameter provided.", 400

        # It's crucial to sanitize user input before using eval().
        # This example lacks proper sanitization and is vulnerable to
        # security risks.  See below for improved security.

        result = eval(user_input)
        return str(result)

    except (NameError, SyntaxError, TypeError, ZeroDivisionError) as e:
        return f"Error: {e}", 400
    except Exception as e: # Catching general exceptions, log for debugging.
        print(f"Unexpected error: {e}") # Log the error for debugging
        return "An unexpected error occurred.", 500


if __name__ == '__main__':
    app.run(debug=True)  # debug=True should only be used during development
```


**Crucially Important Security Considerations:**

The provided solution using `eval()` is extremely dangerous in a real-world application.  `eval()` executes arbitrary code, making your application vulnerable to remote code execution if the `user_input` is not carefully sanitized.  **Never use `eval()` with untrusted input.**

**Safer Alternatives (Highly Recommended):**

1. **ast.literal_eval():**  If you only need to evaluate simple literal expressions (like numbers, strings, lists, dictionaries, etc.), use `ast.literal_eval()`. It's much safer as it only evaluates literal Python structures:

   ```python
   import ast

   @app.route('/')
   def evaluate_expression():
       # ... (get user_input as before)

       try:
           result = ast.literal_eval(user_input)
           return str(result)
       except (SyntaxError, ValueError) as e:
           return f"Error: {e}", 400
       # ... (other exception handling)
   ```