n = int(input())
loads = list(map(int, input().split())) # 도로
villages = list(map(int, input().split())) #마을
result = 0
count = int(1e9)

for i in range(n-1):
    if i == 0:
        result += villages[i] * loads[i]
        count = min(count, villages[i])
    else:
        count = min(count, villages[i])
        result += count * loads[i]
print(result)
