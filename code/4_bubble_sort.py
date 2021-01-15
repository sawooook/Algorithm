n_array = [7,3,4,1,6]

for i in range(len(n_array)):
    for j in range(i, len(n_array)-1):
        if n_array[i] > n_array[j+1]:
            n_array[i], n_array[j+1] = n_array[j+1], n_array[i]
print(n_array)


