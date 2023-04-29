"""
        This module provides a function shuffleseq() which shuffles
        an iterable in such a way that each possible order occurs with equal probability.

        It also provides with another function for testing our function, which verifies
        whether the given sequence is shuffled maintaining its elements and its length.

        Original Author : Pranesh Kumar

        Created On Sat 08 Apr 2023
"""

# We will use the random module to generate
# random indices to test the function
import random


def shuffleseq(data: iter) -> list:
    """This function shuffles the given iterable by converting it into a string
    and then shuffling by swapping it with a random index, so that each possible
    order occurs with equal probability.

    Args:
        data (iter): any kind of iterable which needs to be shuffled

    Returns:
        list: list which consists of the shuffled elements
    """
    seqlen: int = len(data)
    newlist: list = list(data)
    for idx in range(seqlen):
        ridx: int = random.randint(idx, seqlen - 1)
        newlist[idx], newlist[ridx] = newlist[ridx], newlist[idx]
    return newlist


# end of shuffleseq() func.

def test_shuffleseq(seq: iter) -> None:
    """This function checks whether the given sequence is shuffled maintaining
    its elements and its length.

    Args:
        seq (iter): any iterable sequence which needs to be shuffled and tested for.
    """
    shuffled = shuffleseq(seq)
    print("Original:", seq)
    print("Shuffled:", shuffled)
    if set(shuffled) == set(seq) and len(shuffled) == len(seq) and shuffled != seq:
        print("Testcase passed")
    else:
        print("Testcase failed")


# end of test_shuffleseq() func.


# test code
if __name__ == "__main__":
    """
    Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source
    """

    # Testing by providing different sequences manually
    test_shuffleseq([1, 2, 3, 4, 5, 4, 3, 2, 1])
    test_shuffleseq("encryption")
    test_shuffleseq((1.2, 2.4, 3.6, 4.8, 6.0))
    test_shuffleseq({"apple", "banana", "cherry", "dates", "kiwi"})
