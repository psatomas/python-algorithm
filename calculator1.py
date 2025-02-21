def calculator(num1: int, num2: int, op: str) -> str:
    """Performs a basic arithmetic operation on two numbers."""
    if op == '+':
        return f"The addition is {num1 + num2}"
    elif op == '-':
        return f"The subtraction is {num1 - num2}"
    elif op == '*':
        return f"The multiplication is {num1 * num2}"
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return f"The division is {abs(num1 / num2)}"
    else:
        return "Invalid operator"