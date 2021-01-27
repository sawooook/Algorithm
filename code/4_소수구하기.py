# 소수를 구하는 방법은
# 구하고자 하는 수를 자기보다 작은수로 나눠지지 않으면 소수임

n = 100
result = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        result.append(i)
print(result)

n = 100
check_num = [True] * (n+1)
m = int(n ** 0.5)
for i in range(2, m):
    for j in range(i+i, n+1, i):
        if check_num[j] == True:
            check_num[j] = False

for i in range(n+1):
    if check_num[i] == True:
        print(i, end=" ")

# 약수 구하기

n = 12

print("")
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")
print("")

