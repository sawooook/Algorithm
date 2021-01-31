
# 3 - 1
n = int(input("양의정수 N을 입력해주세요: "))
que = []
que.append("1")

while True:
    i = que.pop(0)
    if int(i)%n == 0:
        print(int(i))
        break
    else:
        if i[-1] == '0':
            que.append(i + "0")
        elif i[-1] == '1':
            que.append(i + "0")
            que.append(i + "1")



# 3 - 2
from itertools import combinations

nums = [6,7,9,10,11,13,15,17,19,20,21,22,23,24,25,26,27,30,31,32]
center_num = sum(nums)//2 # 10
difference = int(1e9)
for i in range(len(nums)):
    a = list(combinations(nums, i))
    for i in a:
        left = sum(i)
        right = sum(nums) - sum(i)

        difference = min(abs(left - right), difference)

print(difference)





import copy

nums = [6,7,9,10,11,13,15,17,19,20,21,22,23,24,25,26,27,30,31,32]
sum_nums = sum(nums)
check = [False] * len(nums)
result = int(1e9)

def recur(nums, check):
    global sum_nums
    global result
    for i in range(len(nums)):
        if check[i] == False:
            check[i] = True
            copy_num = nums #7 9 10 11
            copy_num.pop(i)
            left = sum(copy_num)
            right = sum_nums - sum(copy_num)
            result = min(abs(left - right), result)
            recur(copy_num, check)
            check[i] = False

recur(nums,check)
print(result)