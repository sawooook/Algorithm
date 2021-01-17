#- leetcode(1189)
text = list("nlaebolko")
result_text = "balloon"
count = 0
check = True
while check:
    for i in result_text:
        if i in text:
            text.pop(text.index(i))
        else:
            check = False
            break
    else:
        count += 1
else:
    print(count)

#- 이런식으로 for문을 도는것도 좋지만 아래 다른사람 풀이처럼 하면좋을듯
text = "nlaebolko"
d = {"b":0, "a":0, "l":0, "o":0, "n":0}
for e in text:
    if e in d:
        if e == "l" or e == "o":
            d[e] += 0.5
        else:
            d[e] += 1
print(min(d.values()))