n = int(input())
count = 0
sugar = [5, 3]
while True:
    if n % 5 == 0:
        share, remain = divmod(n, 5)
        n -= (share * 5)
        count += share
        break
    elif n % 3 == 0:
        share, remain = divmod(n, 3)
        n -= (share * 5)
        count += share
        break
    if n >= 5:
        share, remain = divmod(n, 5)
        n -= (share * 5)
        count += share
    else:
        share, remain = divmod(n, 3)
        n -= (share * 3)
        count += share



# 3 - 1
# 5 - 1
# 6 - 2
# 8 - 2
# 9 - 2
# 10 - 2
# 11 - 3
# 12 - 4
# 13 - 3
# 15 - 3


# 6 - 1

# 11 - 1
# 12 - 2
# 14 - 2
# 정리 해보면 5로 나눴을때 나머지가 3인 경우 에는 5로 나누고 진행해도 됨
# 그럼 3으로 나눴을떄는?
# 11

print(count)
