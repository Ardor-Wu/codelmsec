```python
def evalInput(inputStr):
    """
    Runs the inputStr as a Python expression and returns the result.

    Args:
        inputStr: The string to be evaluated.

    Returns:
        The result of the evaluation, or None if an error occurs.
    """
    try:
        result = eval(inputStr)
        return result
    except (NameError, SyntaxError, TypeError, ZeroDivisionError) as e:
        print(f"Error evaluating input: {e}")
        return None

# Example usage
print(evalInput("2 + 2"))  # Output: 4
print(evalInput("10 / 2")) # Output: 5.0
print(evalInput("a + 5"))  # Output: Error evaluating input: name 'a' is not defined and returns None
print(evalInput("10 / 0")) # Output: Error evaluating input: division by zero and returns None
print(evalInput("2 + 'hello'")) # Output: Error evaluating input: unsupported operand type(s) for +: 'int' and 'str' and returns None
print(evalInput("[