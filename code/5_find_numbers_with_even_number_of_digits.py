nums = [12, 345, 2, 6, 7896]
result = 0
for i in nums:
    if int(len(str(i))) % 2 == 0:
        result += 1
print(result)