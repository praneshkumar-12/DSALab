"""

    This module provides a function that returns
    a string object, which is an expression where
    the inputs a,b and c satisfy the returned expression.

    It also provides with another function which is
    used to test the checkarithmetic() function.

    Original Author : Pranesh Kumar

    Created On Sat 08 Apr 2023
"""

# We will use the random module to generate
# random values to test the function
import random


def checkarithmetic(a: int, b: int, c: int) -> str:
    """
        Checks whether the given set of inputs satisfy the specified expressions and
        returns the expression as string

        Inputs:
            3 integers a,b and c
        Returns:
            Expression which satisfies the given inputs.
            If no expression is satisfied, "None" is returned
            If the 3 inputs are 0, "All expressions" is returned

    """
    if a == b == c == 0:
        return "All expressions"
    elif a + b == c:
        return "a + b = c"
    elif a + c == b:
        return "a + c = b"
    elif b + c == a:
        return "b + c = a"
    elif a == b - c:
        return "a = b - c"
    elif a == c - b:
        return "a = c - b"
    elif b == a - c:
        return "b = a - c"
    elif b == c - a:
        return "b = c - a"
    elif c == a - b:
        return "c = a - b"
    elif c == b - a:
        return "c = b - a"
    elif a * b == c:
        return "a * b = c"
    elif a * c == b:
        return "a * c = b"
    elif b * c == a:
        return "b * c = a"
    else:
        return "None"


# End of func checkarithmetic()


def testfunction(nooftestcases: int, startvalue: int, endvalue: int) -> None:
    """
        Tests the checkarithmetic() function by providing random values for
        a,b and c within the limits startvalue and endvalue.

        Stores the result in a dictionary, where the key is a tuple
        of values of a,b and c and the value is the expression returned by the function

        startvalue and endvalue specifies the range of random values to be generated
        nooftestcases refers to the number of testcases to be tested

        Inputs:
            nooftestcases : int
            startvalue : int
            endvalue : int

        Returns:
            None

    """
    testcases: dict = {}
    for _ in range(nooftestcases):
        a: int = random.randint(startvalue, endvalue)
        b: int = random.randint(startvalue, endvalue)
        c: int = random.randint(startvalue, endvalue)
        testcases[(a, b, c)] = checkarithmetic(a, b, c)

    print("The testcases are:")
    for key, value in testcases.items():
        print(f"{key} : {value}")


# End of func testfunction()


# Testing code
if __name__ == "__main__":
    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.

    # using our function to test the checkarithmetic() func
    testfunction(nooftestcases=20,
                 startvalue=0,
                 endvalue=20)

    # manually entering values for a, b and c and then testing
    num1: int = int(input("Enter the value for A: "))
    num2: int = int(input("Enter the value for B: "))
    num3: int = int(input("Enter the value for C: "))
    print(checkarithmetic(num1, num2, num3))
