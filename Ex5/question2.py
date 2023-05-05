"""
    This module provides functionality for checking the number of comparisons,
    number of swappings and the time taken for sorting for various sizes of arrays.

    This output can be used for ratio analysis of algorithms by taking n as the size of the array.

    Original Author: Pranesh Kumar

    Created on: 03 May 2023
"""

# importing the necessary modules
import timeit
import random


def insertionsort(seq):
    """
    This function sorts the given sequence and returns a new sorted sequence based on insertion sorting.

    Args:
        seq (Iterable): Sequence to be sorted

    Returns:
        List: Sorted sequence
    """

    start = timeit.default_timer()  # setting the start time

    myseq = seq
    seqlen = len(seq)
    comparisoncount = 0
    overwritecount = 0

    for idx in range(1, seqlen):  # outer for loop for iterating through the elements
        key = myseq[idx]
        j = idx - 1
        while j >= 0 and seq[j] > key:  # inner loop which sorts the elements before it based on some conditions
            comparisoncount += 1
            myseq[j + 1] = myseq[j]
            overwritecount += 1
            j -= 1
        myseq[j + 1] = key # shifts the elements to the right and inserts the element at the right position

    exectime = timeit.default_timer() - start  # finding the time taken

    runtimedata = {"comparisons": comparisoncount, "overwrite": overwritecount,
                   "exec": exectime}  # dictionary of runtime data

    return myseq, runtimedata


# driver code
if __name__ == "__main__":
    f = open("insertionsort.txt", "w")
    sizes = [1, 10, 50, 100, 500, 1000, 5000, 10000]
    for size in sizes:
        comparisons = 0.0
        overwrites = 0.0
        executiontime = 0.0
        testcasecount = 5
        for i in range(testcasecount):
            mylist = [random.randint(-10000, 10000) for _ in range(size)]

            runningdata = insertionsort(mylist.copy())[1]
            comparisons += runningdata['comparisons']
            overwrites += runningdata['overwrite']
            executiontime += runningdata['exec']

        print("==========================Insertion Sort========================", file=f)
        print("================================================================", file=f)
        print(f"Size: {size}", file=f)
        print(f"Number of comparisons: {comparisons / testcasecount}", file=f)
        print(f"Number of overwritings: {overwrites / testcasecount}", file=f)
        print(f"Execution time: {executiontime / testcasecount}", file=f)
        print("================================================================", file=f)

    print("Best Case for size 10".center(64, "="), file=f)
    mylist = [random.randint(-10000, 10000) for _ in range(10)]
    mylist.sort()

    runningdata = insertionsort(mylist.copy())[1]

    print("==========================Insertion Sort========================", file=f)
    print("================================================================", file=f)
    print(f"Size: 10", file=f)
    print(f"Number of comparisons: {runningdata['comparisons']}", file=f)
    print(f"Number of overwritings: {runningdata['overwrite']}", file=f)
    print(f"Execution time: {runningdata['exec']}", file=f)
    print("================================================================", file=f)

    print("Worst Case for size 10".center(64, "="), file=f)
    mylist = [random.randint(-10000, 10000) for _ in range(10)]
    mylist.sort(reverse=True)

    runningdata = insertionsort(mylist.copy())[1]

    print("==========================Bubble Sort===========================", file=f)
    print("================================================================", file=f)
    print(f"Size: 10", file=f)
    print(f"Number of comparisons: {runningdata['comparisons']}", file=f)
    print(f"Number of overwritings: {runningdata['overwrite']}", file=f)
    print(f"Execution time: {runningdata['exec']}", file=f)
    print("================================================================", file=f)

    f.close()
