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


def bubblesort(seq, reverse=False):
    """This function sorts the given sequence and returns a new sorted sequence based on bubble sorting.

    Args:
        seq (Iterable): Sequence to be sorted
        reverse (bool, optional): It should be set as True if the sequence is to be sorted in descending order. Defaults to False.

    Returns:
        List: Sorted sequence
    """
    start = timeit.default_timer() # setting the start time

    myseq = seq
    seqlen = len(seq)
    comparisoncount = 0
    swappingcount = 0

    for i in range(seqlen-1): # outer for loop for iterating through the elements
        for j in range(seqlen-i-1): # inner for loop for number of passes for each iteration
            if reverse: # if reverse is True, then sort in descending
                comparisoncount += 1
                if myseq[j] < myseq[j+1]:
                    swappingcount += 1
                    myseq[j], myseq[j+1] = myseq[j+1], myseq[j] # swapping the current element and the next element
            else: # if reverse is False, then sort in ascending
                comparisoncount += 1
                if myseq[j] > myseq[j+1]:
                    swappingcount += 1
                    myseq[j], myseq[j+1] = myseq[j+1], myseq[j] # swapping the current element and the next element

    exectime = timeit.default_timer() - start # finding the time taken

    runtimedata = {"comparisons": comparisoncount, "swappings": swappingcount, "exec": exectime} # dictionary of runtime data

    return myseq, runtimedata

def selectionsort(seq, reverse=False):
    """This function sorts the given sequence and returns a new sorted sequence based on selection sorting.

    Args:
        seq (Iterable): Sequence to be sorted
        reverse (bool, optional): It should be set as True if the sequence is to be sorted in descending order. Defaults to False.

    Returns:
        List: Sorted Sequence
    """
    start = timeit.default_timer() # setting the start time

    seqlen = len(seq)
    comparisoncount = 0
    swappingcount = 0

    for i in range(seqlen): # iterating through the list
        min_idx = i # setting the minimum index(element) as the first index(element)
        for j in range(i+1, seqlen): # eliminating the previous index element as it is already sorted
            if reverse:  # if reverse is True, then sort in ascending
                comparisoncount += 1
                if seq[j] > seq[min_idx]:
                    min_idx = j
            else:  # if reverse is False, then sort in ascending
                comparisoncount += 1
                if seq[j] < seq[min_idx]:
                    min_idx = j
        swappingcount += 1
        seq[i], seq[min_idx] = seq[min_idx], seq[i] # Swapping current element and the relative first element

    exectime = timeit.default_timer() - start # finding the time taken

    runtimedata = {"comparisons": comparisoncount, "swappings": swappingcount, "exec": exectime} # dictionary of runtime data
    
    return seq, runtimedata
    
# driver code
if __name__ == "__main__": 
    f = open("sorting.txt", "w")
    sizes = [1,10,50, 100,500,1000,5000,10000]
    for size in sizes:
        bcomparisons = 0.0
        bswappings = 0.0
        bexecutiontime = 0.0
        scomparisons = 0.0
        sswappings = 0.0
        sexecutiontime = 0.0
        testcasecount = 5
        for i in range(testcasecount):
            mylist = [random.randint(-10000, 10000) for _ in range(size)]

            brunningdata = bubblesort(mylist.copy())[1]
            bcomparisons += brunningdata['comparisons']
            bswappings += brunningdata['swappings']
            bexecutiontime += brunningdata['exec']

            srunningdata = selectionsort(mylist.copy())[1]
            scomparisons += srunningdata['comparisons']
            sswappings += srunningdata['swappings']
            sexecutiontime += srunningdata['exec']
        print("==========================Bubble Sort===========================", file = f)
        print("================================================================", file = f)
        print(f"Size: {size}", file = f)
        print(f"Number of comparisons: {bcomparisons/testcasecount}", file = f)
        print(f"Number of swappings: {bswappings/testcasecount}", file = f)
        print(f"Execution time: {bexecutiontime/testcasecount}", file = f)
        print("================================================================", file = f)

        print("==========================Selection Sort========================", file = f)
        print("================================================================", file = f)
        print(f"Size: {size}", file = f)
        print(f"Number of comparisons: {scomparisons/testcasecount}", file = f)
        print(f"Number of swappings: {sswappings/testcasecount}", file = f)
        print(f"Execution time: {sexecutiontime/testcasecount}", file = f)
        print("================================================================", file = f)

    print("Best Case for size 10".center(64, "="), file = f)
    mylist = [random.randint(-10000, 10000) for _ in range(10)]
    mylist.sort()

    brunningdata = bubblesort(mylist.copy())[1]
    srunningdata = selectionsort(mylist.copy())[1]

    print("==========================Bubble Sort===========================", file = f)
    print("================================================================", file = f)
    print(f"Size: 10", file = f)
    print(f"Number of comparisons: {brunningdata['comparisons']}", file = f)
    print(f"Number of swappings: {brunningdata['swappings']}", file = f)
    print(f"Execution time: {brunningdata['exec']}", file = f)
    print("================================================================", file = f)

    print("==========================Selection Sort===========================", file = f)
    print("================================================================", file = f)
    print(f"Size: 10", file = f)
    print(f"Number of comparisons: {srunningdata['comparisons']}", file = f)
    print(f"Number of swappings: {srunningdata['swappings']}", file = f)
    print(f"Execution time: {srunningdata['exec']}", file = f)
    print("================================================================", file = f)

    print("Worst Case for size 10".center(64, "="), file = f)
    mylist = [random.randint(-10000, 10000) for _ in range(10)]
    mylist.sort(reverse=True)

    brunningdata = bubblesort(mylist.copy())[1]
    srunningdata = selectionsort(mylist.copy())[1]

    print("==========================Bubble Sort===========================", file = f)
    print("================================================================", file = f)
    print(f"Size: {size}", file = f)
    print(f"Number of comparisons: {brunningdata['comparisons']}", file = f)
    print(f"Number of swappings: {brunningdata['swappings']}", file = f)
    print(f"Execution time: {brunningdata['exec']}", file = f)
    print("================================================================", file = f)

    print("==========================Selection Sort===========================", file = f)
    print("================================================================", file = f)
    print(f"Size: {size}", file = f)
    print(f"Number of comparisons: {srunningdata['comparisons']}", file = f)
    print(f"Number of swappings: {srunningdata['swappings']}", file = f)
    print(f"Execution time: {srunningdata['exec']}", file = f)
    print("================================================================", file = f)

    f.close()
