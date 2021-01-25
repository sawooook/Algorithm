list = [1,5,3,4,2]


def merge(left, right):
    i = 0
    j = 0
    arr = []
    while(i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        elif j < len(right):
            arr.append(right[j])
            j += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    return arr

def sorted_merge(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left_list = list[:mid]
    right_list = list[mid:]
    left = sorted_merge(left_list)
    right = sorted_merge(right_list)
    return merge(left, right)

print(sorted_merge(list))