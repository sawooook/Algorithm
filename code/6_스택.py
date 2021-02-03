prices = [1,2,3,2,3]
result = []
count = 0
while prices:
    count = 0
    out_num = prices.pop(0)
    for i in prices:
        if i >= out_num:
            print(i, out_num)
            count += 1
        else:
            count += 1

            result.append(count)
            break
    else:
        result.append(count)
print(result)

if i == "0" or i == "2" or i == "4" or i == "8" or i == "9":
    for i in range(2):
        print(array[1])
