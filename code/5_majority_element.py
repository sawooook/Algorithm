from collections import Counter
nums = [2,2,1,1,1,2,2]

nums_index = (len(nums)//2)+1
count_array = Counter(nums)
result = 0
for i in count_array.items():
    if i[1] >= nums_index:
        nums_index = i[1]
        result = i[0]

print(result)