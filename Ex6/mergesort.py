def merge(seq1, seq2):
    i = j = 0
    m = len(seq1)
    n = len(seq2)
    result = []
    while (i<m and j<n):
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