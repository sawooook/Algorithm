n ,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
result = 0
for i in graph:
    result = max(min(i), result)

print(result)

# 처음 내풀이
# 리뷰는 ,,, graph로 받을 때 처리해도 좋을 꺼같음

n ,m = map(int, input().split())
result = 0
for i in range(n):
    graph = list(map(int, input().split()))
    result = max(min(graph), result)
print(result)