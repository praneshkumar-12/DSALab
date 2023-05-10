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


if __name__ == "__main__":
    import random 
    sizes = [1, 10, 50, 100, 500, 1000, 5000, 10000]
    for size in sizes:
        myseq = [random.randint(-10000, 10000) for _ in range(size)]
        mergesort(myseq)
        print("="*50)
        print(f"Size: {size} \n Number of comparisons: {count}")
        print("="*50)