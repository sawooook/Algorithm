n_array = [7,3,4,5,1,9]

for i in range(1, len(n_array)):
    for j in range(len(n_array)-1, i, -1):
        if n_array[j] > n_array[j-1]:
            n_array[j], n_array[j-1] = n_array[j-1], n_array[j]

print(n_array)