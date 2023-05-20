"""
This module provides functionality for sorting a sequence using quicksort and analyse
the time complexity by using the number of comparisons as f(n)

Original Author: Pranesh Kumar

Created on: 20 May 2023
"""

import random

count = 0


def qsort(seq, begin, end):
    """
    This functions sorts a sequence using quicksort algorithm recursively.
    Sorts the original sequence.
    Original sequence gets changed.
    Args:
        begin: Starting index from which sorting is to be done
        end: Ending index up to which sorting is to be done.
        seq: Iterable which needs to be sorted

    Returns:
        None
    """
    if begin < end:
        k = partition(seq, begin, end - 1)
        qsort(seq, begin, k - 1)
        qsort(seq, k + 1, end)


def partition(seq, begin, end):
    """
    Partitions a list based on a pivot so that the elements on the left of pivot
    is less than pivot and elements on the right of pivot is greater than the pivot.

    This function returns the middle element/ the index of the pivot in the list
    Args:
        seq: sequence which needs to be partitioned based on pivot
        begin: starting index from which portioning is to be done
        end: ending index up to which portioning is to be done

    Returns:
        i (int): the index of pivot element in the sequence
    """
    global count
    find_median(begin, end, seq)
    pivot = seq[end]
    i = begin - 1
    for j in range(begin, end):
        count += 1
        if seq[j] <= pivot:
            i += 1

            seq[i], seq[j] = seq[j], seq[i]

    seq[i+1], seq[end] = seq[end], seq[i+1]

    return i+1


def find_median(begin, end, seq):
    """
    This function finds the median element and movies it to the end of the list, so that
    it can be the pivot while using in the partition function.

    This changes the original sequence

    Args:
        begin: starting index from which median is to be found
        end: ending index up to which median is to be found
        seq: sequence of which median is to be found

    Returns:
        None
    """
    mid = (begin + end) // 2
    if seq[begin] > seq[mid]:
        seq[begin], seq[mid] = seq[mid], seq[begin]
    if seq[mid] > seq[end]:
        seq[mid], seq[end] = seq[end], seq[mid]
    if seq[begin] > seq[end]:
        seq[begin], seq[end] = seq[end], seq[begin]

    seq[mid], seq[end] = seq[end], seq[mid]


# driver code
if __name__ == "__main__":
    sizes = [1, 10, 50, 100, 500, 1000, 5000, 10000]
    for size in sizes:
        # size = int(input("Enter the size of list: "))
        my_seq = [random.randint(-10000, 10000) for _ in range(size)]
        qsort(my_seq, 0, size)
        print(my_seq)
        print(size, count)
        count = 0
