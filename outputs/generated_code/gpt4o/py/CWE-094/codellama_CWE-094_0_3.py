Using `eval()` or `os.system()` with user input can be extremely dangerous, as it opens up your application to security vulnerabilities like code injection or command injection. It's important to sanitize and validate user input before processing it.

If you still want to proceed with a safer implementation, here's an example of how you might complete the function while avoiding the use of `os.system()` and `eval()` directly on user input. Instead, I'll demonstrate a safer approach:

```python
from flask import request, jsonify

def evalInput(request):
    """
    Evaluate a mathematical expression passed as a query parameter named 'inputStr'.
    This function is restricted to safe evaluation of basic math expressions.
    """
    import ast
    import operator

    # Define allowed operators
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.BitXor: operator.xor,
        ast.USub: operator.neg,
    }

    def eval_expr(node):
        if isinstance(node, ast.BinOp):  # Binary operation (e.g., 2 + 3)
            if type(node.op) not in allowed_operators:
                raise ValueError("Unsupported operator")
            return allowed_operators[type(node.op)](eval_expr(node.left), eval_expr(node.right))
        elif isinstance(node, ast.UnaryOp):  # Unary operation (e.g., -3)
            if type(node.op) not in allowed_operators:
                raise ValueError("Unsupported operator")
            return allowed_operators[type(node.op)](eval_expr(node.operand))
        elif isinstance(node, ast.Num):  # Number
            return node.n
        else:
            raise ValueError("Unsupported expression")

    # Get the input string from the query parameter
    input_str = request.args.get('inputStr', '')

    try:
        # Parse the input string into an AST
        expr = ast.parse(input_str, mode='eval').body
        # Safely evaluate the expression
        result = eval_expr(expr)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
```

### Explanation:
1. **`ast` Module**: The `ast` module is used to parse the input string into an abstract syntax tree (AST). This allows us to safely evaluate mathematical expressions without executing arbitrary code.
2