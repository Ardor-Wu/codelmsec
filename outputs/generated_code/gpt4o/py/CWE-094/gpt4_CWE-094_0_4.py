```python
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
```

### **Important Security Note:**
Using `eval()` to evaluate user input is **extremely dangerous** because it can execute arbitrary code, potentially leading to security vulnerabilities. For example, a malicious user could pass input like `__import__('os').system('rm -rf /')` to execute harmful commands.

If you need to evaluate user input safely, consider using a library like `asteval` or implementing a custom parser for the specific expressions you want to support. Always validate and sanitize user input thoroughly.