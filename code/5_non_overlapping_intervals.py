input = [[1,2], [2,3], [4,5]]

input.sort()
prev = float("-inf")
count = 0
for i in input:
    if i[0] >= prev:
        prev = i[1]
    else:
        count += 1
        prev = min(prev, i[1])
print(count)