prices = [7,1,5,3,6,4]
if not prices or len(prices) is 1:
    print(0)
profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        profit += prices[i] - prices[i - 1]
print(profit)


## 내가 그리디 알고리즘에 대해서 잘모르는듯 ,,,
