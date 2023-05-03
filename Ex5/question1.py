import timeit
import random

def bubblesort(seq, reverse=False):
    start = timeit.default_timer()
    myseq = seq
    seqlen = len(seq)
    comparisoncount = 0
    swappingcount = 0
    for i in range(seqlen-1):
        for j in range(seqlen-i-1):
            if reverse:
                comparisoncount += 1
                if myseq[j] < myseq[j+1]:
                    swappingcount += 1
                    myseq[j], myseq[j+1] = myseq[j+1], myseq[j]
            else:
                comparisoncount += 1
                if myseq[j] > myseq[j+1]:
                    swappingcount += 1
                    myseq[j], myseq[j+1] = myseq[j+1], myseq[j]
    exectime = timeit.default_timer() - start
    runtimedata = {"comparisons": comparisoncount, "swappings": swappingcount, "exec": exectime}
    return myseq, runtimedata

def selectionsort(seq, reverse=False):
    start = timeit.default_timer()
    seqlen = len(seq)
    myseq = seq
    comparisoncount = 0
    swappingcount = 0
    for i in range(seqlen):
        min_idx = i
        for j in range(i+1, seqlen):
            if reverse:
                comparisoncount += 1
                if myseq[j] > myseq[min_idx]:
                    min_idx = j
            else:
                comparisoncount += 1
                if myseq[j] < myseq[min_idx]:
                    min_idx = j
        swappingcount += 1
        myseq[i], myseq[min_idx] = myseq[min_idx], myseq[i]
    exectime = timeit.default_timer() - start
    runtimedata = {"comparisons": comparisoncount, "swappings": swappingcount, "exec": exectime}
    return myseq, runtimedata
    

if __name__ == "__main__": 
    f = open("sorting.txt", "w")
    sizes = [1,10,50,100,500,1000,5000,10000]
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

            brunningdata = bubblesort(mylist)[1]
            bcomparisons += brunningdata['comparisons']
            bswappings += brunningdata['swappings']
            bexecutiontime += brunningdata['exec']

            srunningdata = selectionsort(mylist)[1]
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

    brunningdata = bubblesort(mylist)[1]
    srunningdata = selectionsort(mylist)[1]

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

    brunningdata = bubblesort(mylist)[1]
    srunningdata = selectionsort(mylist)[1]

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
