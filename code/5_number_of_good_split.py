from collections import Counter
s = "aacaba"

# s1 = { a: 1, c:1}
# s2 = {a:3  ,b:1}

count_s = Counter(s)
dic = Counter()
result = 0
for i in s:
    count_s[i] -= 1
    dic[i] += 1

    if count_s[i] == 0:
        count_s.pop(i)

    if len(count_s) == len(dic):
        result += 1
print(result)