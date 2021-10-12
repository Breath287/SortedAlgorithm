def quickSort(lis, l, r):
    if l >= r:
        return lis

    pivot = lis[l]
    low, high = l, r
    while l < r:
        while l < r and lis[r] >= pivot:
            r -= 1
        lis[l] = lis[r]

        while l < r and lis[l] < pivot:
            l += 1
        lis[r] = lis[l]
    lis[r] = pivot
    quickSort(lis, low, l-1)
    quickSort(lis, l+1, high)
    return lis


arr = [2,33,12,44,21,44]
print(quickSort(arr, 0, len(arr)-1))
