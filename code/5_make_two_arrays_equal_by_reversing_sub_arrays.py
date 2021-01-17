#- leetcode(1460)
from collections import Counter
target = [1,2,2]
arr = [1,1,2]

if Counter(arr) == Counter(target):
    print("true")
else:
    print("FALSE")

#- 배열안의 숫자의 개수를 파악할땐 Counter를 사용하면 좋을듯