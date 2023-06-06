class Stack:
    """Stack implementation using a list"""

    def __init__(self):
        """Initialize an empty stack"""
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def push(self, item):
        """Push an item onto the stack"""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """Return the top item on the stack without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]


def infix_to_postfix(expression):
    """Convert an infix expression to postfix notation"""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}  # Operator precedence

    postfix = ""
    stack = Stack()

    for char in expression:
        if char.isalnum():  # Operand
            postfix += char
        elif char == "(":  # Opening parenthesis
            stack.push(char)
        elif char == ")":  # Closing parenthesis
            while not stack.is_empty() and stack.peek() != "(":
                postfix += stack.pop()
            stack.pop()  # Pop the opening parenthesis
        else:  # Operator
            while not stack.is_empty() and stack.peek() != "(" and precedence[char] <= precedence[stack.peek()]:
                postfix += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix


def evaluate_postfix(expression):
    """Evaluate a postfix expression"""
    stack = Stack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.push(result)

    return stack.pop()


def perform_operation(operand1, operand2, operator):
    """Perform arithmetic operation"""
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^":
        return operand1 ** operand2
    else:
        raise ValueError("Invalid operator")


# Example usage

expression = "(2+3)*4-9/3^2"
postfix_expression = infix_to_postfix(expression)
result = evaluate_postfix(postfix_expression)
print("Infix Expression:", expression)
print("Postfix Expression:", postfix_expression)
print("Result:", result)
