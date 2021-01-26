nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1_len = len(nums1)
nums2_len = len(nums2)

result = []
if nums1_len > nums2_len:
    for i in nums2:
        if i in nums1 and not i in result:
            result.append(i)
else:
    for i in nums1:
        if i in nums2 and not i in result:
            result.append(i)
print(result)


# 다른 사람풀이
list(set(nums1) & set(nums2))
# set을 이용하면 중복을 제거하고 set에다가 &를 쓰면 교집합 찾을수있음