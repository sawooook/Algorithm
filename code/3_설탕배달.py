sugar = int(input())
count = 0

while True:
    if (sugar % 5) == 0:
        a, b = divmod(sugar, 5)
        count += a
        break
    sugar -= 3
    count += 1
    if sugar < 0:
        print("-1")
        break
else:
    print(count)