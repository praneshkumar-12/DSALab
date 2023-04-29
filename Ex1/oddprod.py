"""
    This module provides a function checkproduct() that returns a tuple object
    which consists of:
        1. count - refers to the number of combinations required to produce an odd product
        2. tuple - refers to the tuple that contains the elements which are multiplied
        3. product - refers to the product after multiplying the numbers in the tuple

    It also consists of a function that tests our function, with random lists and
    checks it with the output produced with the help of built-in functions.

    Original Author : Pranesh Kumar

    Created On Sat 08 Apr 2023
"""

# We will use the random module to generate
# random values to test the function
import random

# We will use the itertools module to test the output produced
# by our function
from itertools import product


def checkoddproduct(seq: iter) -> tuple[int, tuple, int]:
    """This function provides a way to check the number of combinations or pairs
    required to produce an odd product.

    Args:
        seq (iter): can be any indexed iterable

    Returns:
        tuple[int, tuple, int]: tuple consisting of 3 elements:
        1. count - number of pairs required
        2. tuple - numbers in the pair
        3. product - product of the numbers in the pair
    """
    count: int = 0
    for i in seq:
        for j in seq:
            count += 1
            if (i * j) % 2 != 0:
                return count, (i, j), i * j


# end of checkoddproduct() func


def createrandomlist(size: int = 10, startvalue: int = -10000, endvalue: int = 10000) -> list:
    """This function creates a list of specified size with values ranging from
    the specified start and end values

    Args:
        size (int, optional): length of the required list. Defaults to 10.
        startvalue (int, optional): starting range for generating random value. Defaults to -10000.
        endvalue (int, optional): ending range for generating random value. Defaults to 10000.

    Returns:
        list: list with the required number of values within the specified range
    """
    randomlist: list = []
    for count in range(size):
        randomlist.append(random.randint(startvalue, endvalue))
    return randomlist


# End of createrandomlist() func


def testfunction(nooftestcases: int) -> None:
    """This function tests the checkoddprod() function, by testing it with
    random lists with the help of createrandomlist() function for specified number
    of times.

    Also checks if the returned value matches with the value generated with
    the help of built-in functions. If it does not match, it prints a
    message.

    Args:
        nooftestcases (int): number of testcases to be tested
    """
    for count in range(nooftestcases):
        testlist = createrandomlist()
        answer: tuple = checkoddproduct(testlist)
        combinedseq = list(product(testlist, testlist))
        rightanswer = ()
        for idx, elt in enumerate(combinedseq):
            if (elt[0] * elt[1]) % 2 != 0:
                rightanswer: tuple = idx + 1, (elt[0], elt[1]), elt[0] * elt[1]
                break
        print(answer, rightanswer, sep=" -- ")
        if answer != rightanswer:
            print("Function has returned a wrong answer!")


# End of testfunction() func


if __name__ == "__main__":
    """Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source
    """

    # Manual testing
    print(checkoddproduct([1, 6, 4, 7, 8]))
    print(checkoddproduct([2, 4, 6, 8, 10]))
    try:
        print(checkoddproduct(['ABCDE'])) # strings won't work here
    except Exception as e:
        print(e)
    print(checkoddproduct((10, 3, 45, 98, 100)))
    print(checkoddproduct({10, 3, 45, 98, 100})) # sets would work

    # using our function to test
    testfunction(nooftestcases=15)
