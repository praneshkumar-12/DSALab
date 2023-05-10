import random

count = 0

def merge(seq1, seq2):
    global count
    i = j = 0
    m = len(seq1)
    n = len(seq2)
    result = []
    while (i<m and j<n):
        count += 1
        if seq1[i] < seq2[j]:
            result.append(seq1[i])
            i += 1
        else:
            result.append(seq2[j])
            j += 1
    while (i<m):
        result.append(seq1[i])
        i += 1
    while (j<n):
        result.append(seq2[j])
        j += 1
    return result

def mergesort(seq):
    length = len(seq)
    if (length < 2):
        return (seq[:])
    else:
        mid = length // 2
        return merge(mergesort(seq[:mid]), mergesort(seq[mid:]))

def bestcasecomplexity(size):
    myseq = [random.randint(-10000, 10000) for _ in range(size)]
    myseq.sort()
    mergesort(myseq)

def worstcasecomplexity(size):
    myseq = [random.randint(-10000, 10000) for _ in range(size)]
    myseq.sort(reverse=True)
    mergesort(myseq)


if __name__ == "__main__":
    sizes = [1, 10, 50, 100, 500, 1000, 5000, 10000]
    for size in sizes:
        count = 0
        myseq = [random.randint(-10000, 10000) for _ in range(size)]
        mergesort(myseq)
        print("="*50)
        print(f"Size: {size} \nNumber of comparisons: {count}")
        print("="*50)

    count = 0
    bestcasecomplexity(10)
    print("="*50)
    print(f"Best Case - Size: {10} \nNumber of comparisons: {count}")
    print("="*50)

    count = 0
    worstcasecomplexity(10)
    print("="*50)
    print(f"Worst Case - Size: {10} \nNumber of comparisons: {count}")
    print("="*50)