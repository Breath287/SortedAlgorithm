def shellSort(lis):
    length = len(lis)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = lis[i]
            j = i
            if lis[j-gap] > temp:
                lis[j] = lis[j-gap]
                j -= gap
            lis[j] = temp
        gap //= 2

    return lis


print(shellSort([1,33,22,34,45,112]))

