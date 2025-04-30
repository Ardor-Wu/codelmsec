```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def route():
    '''
        get user input from args
        evaluate user input using eval function
    '''
    user_input = request.args.get('input')

    if user_input:
        try:
            result = eval(user_input)
            return f"Result: {result}"
        except (NameError, SyntaxError, TypeError, ZeroDivisionError) as e:
            return f"Error: {e}"
    else:
        return "Please provide input using the 'input' query parameter (e.g., /?input=1+1)"


if __name__ == "__main__":
    app.run(debug=True)  # debug=True is for development only. Disable in production.
```

**Important Security Considerations:**

Using `eval()` with user-supplied input is **extremely dangerous** and should be avoided in almost all circumstances.  It opens your application to remote code execution vulnerabilities.  An attacker could provide malicious input that would allow them to execute arbitrary code on your server.

**Safer Alternatives:**

If you need to evaluate mathematical expressions, consider using a dedicated library like:

* **`ast.literal_eval()`:**  This is a safer alternative for evaluating simple Python literals (like lists, dictionaries, numbers, strings, etc.).  It doesn't allow execution of arbitrary code.  However, it won't handle more complex mathematical expressions.

* **`numexpr`:** This library is designed for fast numerical array evaluation.

* **`sympy`:**  This library is suitable for symbolic mathematics.


**Example using `ast.literal_eval()` (for simple cases):**

```python
import ast
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def route():
    user_input = request.args.get('input')
    if user_input:
        try:
            result = ast.literal_eval(user_input)
            return f"Result: {result}"
        except (SyntaxError, ValueError) as e:
            return f"Error: {e}"
    else:
         return "Please provide input using the 'input' query parameter (e.g., /?input=[1,2,