# 프로그래머스
from collections import  deque
prices = deque([1,2,3,2,3])
count = 0
result = []
while prices:
    out_prices = prices.popleft()
    for i in prices:
        if out_prices <= i:
            count +=1
        else:
            count += 1
            break
    result.append(count)
    count = 0
print(result)
## 위에 처럼 푸니까 ,,, 정확성은 다맞는데 효율성 문제가... 그래서 deque로 바꿔서 하니까 잘됨
# 대부분 2중포문으로 하길래 나도 한번 해봄
prices = [1,2,3,2,3]
result = []
count = 0
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] <= prices[j]:
           count += 1
        else:
            count += 1
            break
    result.append(count)
    count = 0


print(result)