"""
This module provides functionality for finding the search element in a sequence by using binary search

Original Author: Pranesh Kumar

Created on 10 May 2023

"""

from mergesort import mergesort

count = 0

def binarysearch(seq, low, high, sval):
    global count
    """
    This function finds the search element in a sequence recursively using binary search
    """
    count += 1
    if low > high:  # base condition
        return -1
    else:
        mid = (low + high) // 2
        count += 1
        if sval == seq[mid]:
            return mid
        count += 1
        if sval < seq[mid]:
            return binarysearch(seq, low, mid - 1, sval)
        else:
            return binarysearch(seq, mid + 1, high, sval)


if __name__ == "__main__":
    import random

    size = int(input("Enter the size of the list: "))
    myseq = [random.randint(-10000, 10000) for _ in range(size)]
    search = random.choice(myseq)
    print(search)
    print(mergesort(myseq))
    print(binarysearch(mergesort(myseq), 0, size, search))
    print(size, count)
