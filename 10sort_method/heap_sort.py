import heapq

def heapSort(lis):
    res = []
    for i in lis:
        heapq.heappush(res, i)
    return [heapq.heappop(res) for i in range(len(res))]

print(heapSort([1,33,22,34,45,112]))
