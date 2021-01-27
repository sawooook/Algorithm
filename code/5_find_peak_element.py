nums = [2,4,8,9,10,1,2,15]
left = 0
right = len(nums) - 1

# left: 0 -> 0 -> 1
# right :5 -> 2
# mid : 2 -> 1
while left < right:
    mid = (left+right)//2
    if nums[mid] < nums[mid+1]:
        left = mid+1
    else:
        right = mid
else:
    print(left)