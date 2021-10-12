def selectSort(lis):
    res = []
    while len(lis) > 0:
        min_num = min(lis)
        res.append(min_num)
        lis.remove(min_num)

    return res

print(selectSort([1,33,22,34,45,112]))
