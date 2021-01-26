import heapq
nums = [-4, -1, 0, 3, 10]
result = []
for i in range(len(nums)):
    if abs(i[0]) > abs(i[-1]):
        j = i[0] ** 2
        result.insert(0, j)
        result.pop(0)
    else:
        j = i[1] ** 2
        result.insert(0, j)
        result.pop(-1)