from collections import Counter
text = "Aabb"

counter_array = Counter(text)
result = ""

for i in sorted(counter_array.items(), key=lambda x:x[1], reverse=True):
    for j in range(i[1]):
        print(i[0], end="")
print("")

# 다른 사람 풀이 나는 O(n^2) 인데 이렇게 하지말고

for k,v in sorted(counter_array.items(), key=lambda x:x[1], reverse=True):
    result += k*v
print(result)

# str * 2 -> 'b' * 2를 하면 'bb'가나옴


text = "Aabb"
dic = {}
result = ""
for i in text:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
    result += k*v
print(result)