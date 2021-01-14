#- 백준 11047번
n ,k = map(int, input().split())
money_lists = []
for i in range(n):
    money_lists.append(int(input()))

count = 0

while k != 0:
    for i in reversed(sorted(money_lists)):
        if k > i:
            share, remain = divmod(k, i)
            k -= (i * share)
            count += share
else:
    print(count)