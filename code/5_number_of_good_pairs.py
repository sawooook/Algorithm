#- leetcode(1512)
nums = [1,2,3,1,1,3]
count = 0

for i in range(len(nums)-1):
    for j in range(i, len(nums)):
        if i < j:
            if nums[i] == nums[j]:
                count += 1
print(count)

#- 무조건 for문을 돌리려고 하지말고 다른 방법으로 생각해보기
# 같은숫자의 개수를 키포인트로 잡고 진행해보자

count = 0
for i in range(len(nums)):
    if nums[:i].count(nums[i]) > 0:
        count += nums[:i].count(nums[i])
print(count)