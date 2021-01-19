#- leetcode(1184)

distance = [1,2,3,4]
start = 0
destination = 1
result = 0
if start + 1 == destination:
    result += (distance[destination - 1])
elif start -1 == destination:
    result += distance[destination]