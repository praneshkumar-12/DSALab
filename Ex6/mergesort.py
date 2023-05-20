"""
    This module provides functionality for checking the execution time and 
    number of comparisons for sorting of various sequences using merge sort

    This output can be used for ratio analysis of algorithms by taking n as the size of the array or
    as the number of comparisons.

    Original Author: Pranesh Kumar

    Created on 10 May 2023
"""

# importing the necessary modules
import random
import timeit

count = 0
starttime = 0


def merge(seq1, seq2):
    """
    This function performs merge operation on the two lists which are passsed to the function.

    Args:
        seq1 (Iterable): First sequence to be merged
        seq2 (Iterable): Second sequence to be merged

    Returns:
        Merged list of seq1 and seq2 which is sorted
    """

    global count
    i = j = 0
    m = len(seq1)
    n = len(seq2)
    result = []
    while i < m and j < n:
        count += 1
        if seq1[i] < seq2[j]:
            result.append(seq1[i])
            i += 1
        else:
            result.append(seq2[j])
            j += 1
    while (i < m):
        result.append(seq1[i])
        i += 1
    while (j < n):
        result.append(seq2[j])
        j += 1
    return result


def mergesort(seq):
    """
    Performs recursive merge operation on list by using divide and conquer technique
    
    Args:
        seq (Iterable) Sequene to be sorted
    
    Returns:
        Sorted sequence
    """
    length = len(seq)
    if length < 2:  # Base Condition
        return seq[:]
    else:
        mid = length // 2
        return merge(mergesort(seq[:mid]), mergesort(seq[mid:]))  # Recursive call


def bestcasecomplexity(size):
    """
    Finds out the best case complexity of merge sort by passing an already sorted list
    """
    myseq = [random.randint(-10000, 10000) for _ in range(size)]
    myseq.sort()
    mergesort(myseq)


def worstcasecomplexity(size):
    """
    Finds out the worst case complexity of merge sort by passing an already sorted list in descending order
    """
    myseq = [random.randint(-10000, 10000) for _ in range(size)]
    myseq.sort(reverse=True)
    mergesort(myseq)


# driver code
if __name__ == "__main__":
    f1 = open("merge-sort-comp.txt", "w")
    f2 = open("merge-sort-time.txt", "w")

    sizes = [1, 10, 50, 100, 500, 1000, 5000, 10000]
    for size in sizes:
        count = 0
        starttime = timeit.default_timer()
        myseq = [random.randint(-10000, 10000) for _ in range(size)]
        mergesort(myseq)
        print("=" * 50, file=f1)
        print(f"Size: {size} \nNumber of comparisons: {count}", file=f1)
        print("=" * 50, file=f1)

        exectime = timeit.default_timer() - starttime
        print("=" * 50, file=f2)
        print(f"Size: {size} \nExecution Time: {exectime}", file=f2)
        print("=" * 50, file=f2)

    count = 0
    starttime = timeit.default_timer()
    bestcasecomplexity(10)
    print("=" * 50, file=f1)
    print(f"Best Case - Size: {10} \nNumber of comparisons: {count}", file=f1)
    print("=" * 50, file=f1)

    exectime = timeit.default_timer() - starttime
    print("=" * 50, file=f2)
    print(f"Best Case - Size: {10} \nExecution Time: {exectime}", file=f2)
    print("=" * 50, file=f2)

    count = 0
    starttime = timeit.default_timer()
    worstcasecomplexity(10)
    print("=" * 50, file=f1)
    print(f"Worst Case - Size: {10} \nNumber of comparisons: {count}", file=f1)
    print("=" * 50, file=f1)

    exectime = timeit.default_timer() - starttime
    print("=" * 50, file=f2)
    print(f"Worst Case - Size: {10} \nExecution Time: {exectime}", file=f2)
    print("=" * 50, file=f2)

    f1.close()
    f2.close()
