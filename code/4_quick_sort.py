## quick Sort

n_array = [7,3,4,1,6]
def quick_sort(n_array):
    if len(n_array) <= 1:
        return n_array

    pivot = n_array[len(n_array)//2]
    left, center, right = [], [], []
    for i in n_array:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            center.append(i)
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort(n_array))