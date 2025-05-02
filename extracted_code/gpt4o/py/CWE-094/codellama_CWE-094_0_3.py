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
