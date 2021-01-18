#- hackerRank
vowel = ["a", "e", "i", "o", "u", "y"]

array = ["programming", "is", "awesome"]
count = 0
result = 0

for sentence in array:
    for alphabet in sentence:
        if alphabet in vowel:
            count += 1
    if count % 2 == 0:
        result += 2
    else:
        result += 1
    count = 0
print(result)