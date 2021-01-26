# 이 문제 결국 못풀음 easy인데 ㅠㅠㅠ
# 이런 문제는 절대값을 이용! 그리고 for문으로 앞에서부터 찾는다는 생각은 버리자
s = "loveleetcode"
c = "e"

pos = []
res = []

for i in range(len(s)):
    if s[i] == c:
        pos.append(i)
# e의 index값을 저장

# 0
for i in range(len(s)):
    mn = len(s)
    for p in pos:
        # 3 5 6 12
        mn = min(mn, abs(i-p))
    res.append(mn)
print(res)