def mergeSort(lis):
    if len(lis) == 1:
        return lis
    length = len(lis)
    mid = length // 2

    left = mergeSort(lis[:mid])
    right = mergeSort(lis[mid:])

    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]
    return res


print(mergeSort([2,34,23,4,1,33,44]))