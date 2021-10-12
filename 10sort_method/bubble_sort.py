def bubbleSort(lis):
    length = len(lis)
    for i in range(length):
        for j in range(i+1, length):
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis[j], lis[i]

    return lis

print(bubbleSort([2,44,22,12,45]))
