"""
This module provides functionality for finding the search element in a sequence by using binary search

Original Author: Pranesh Kumar

Created on 10 May 2023

"""

from mergesort import mergesort


def binarysearch(seq, low, high, sval):
    """
    This function finds the search element in a sequence recursively using binary search
    """

    if low > high:  # base condition
        return -1
    else:
        mid = (low + high) // 2
        if sval == seq[mid]:
            return mid
        elif sval < seq[mid]:
            return binarysearch(seq, low, mid - 1, sval)
        else:
            return binarysearch(seq, mid + 1, high, sval)


if __name__ == "__main__":
    import random

    size = 10
    myseq = [random.randint(-10000, 10000) for _ in range(size)]
    mergesort(myseq)
    search = random.choice(myseq)
    print(search)
    print(binarysearch(sorted(myseq), 0, size, search))
