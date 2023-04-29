"""

    This module provides a function that returns
    a tuple object, which contains the minimum element
    followed by the maximum element in the given sequence

    It also provides with another function which is
    used to test the finminmax() function.

    Original Author : Pranesh Kumar

    Created On Sat 08 Apr 2023
"""

# We will use the random module to generate
# random values to test the function
import random


def findminmax(seq: list) -> tuple:
    """This function returns a tuple which contains the minimum element
    followed by the maximum element.
    Returns a tuple with None, when the sequence is empty.
    Returns a tuple with same values, when the sequence is singleton.


    Args:
        seq (list): input sequence which can be any indexed iterable,
                        preferably a list

    Returns:
        tuple: tuple which contains the minimum element followed by the maximum
                element

    """
    seqsize = len(seq)
    comparisonCount: int = 0
    if seqsize == 0:
        return None, comparisonCount
    elif seqsize == 1:
        return seq[0], seq[0], comparisonCount
    elif seqsize == 2:
        if seq[0] < seq[1]:
            return seq[0], seq[1], comparisonCount
        else:
            return seq[1], seq[0], comparisonCount
    else:
        minelt = seq[0]
        maxelt = seq[0]
        for idx in range(1, seqsize):
            if seq[idx] > maxelt:
                comparisonCount += 1
                maxelt = seq[idx]
            elif seq[idx] < minelt:
                comparisonCount += 1
                minelt = seq[idx]
        return minelt, maxelt, comparisonCount


# End of findminmax() func

def createrandomlist(size: int = 1000, startvalue: int = -10000, endvalue: int = 10000) -> list:
    """This function creates a list of specified size with values ranging from
    the specified start and end values

    Args:
        size (int, optional): length of the required list. Defaults to 1000.
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
    """This function tests the findminmax() function, by testing it with
    random lists with the help of createrandomlist() function for specified number
    of times.

    Also checks if the returned value matches with the value generated with
    the help of built-in functions. If it does not match, it prints a
    message.

    Args:
        nooftestcases (int): number of testcases to be tested
    """
    for count in range(nooftestcases):
        mySize = count + (10 * (count + 1 ))
        testlist = createrandomlist(size = mySize)
        answer: tuple = findminmax(testlist)
        rightanswer: tuple = min(testlist), max(testlist)
        print(mySize, answer, rightanswer)
        if answer[0:2] != rightanswer:
            print("Function has returned a wrong answer!")


# End of testfunction() func


# Testing code
if __name__ == "__main__":
    """Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source
    """

    # Manual testing
    print(findminmax([]))
    print(findminmax([100]))
    try:
        print(findminmax({1, 2, 3, 4}))  # sets does not work with our function
    except Exception as e:
        print(e)
    finally:
        print(findminmax("Hello!"))

    # using our function to test
    testfunction(nooftestcases=10)
