n = 7
array = [
"UK",
"China",
"USA",
"France",
"New Zealand",
"UK",
"France",
]

print(len(set(array)))



# 다른 사람들 풀이 array를 받고 푸는것이 아니라
# set을 만들어서 포문을 돌면서 중복 제거
s = set()
for i in range(n):
    s.add(i)
print(len(s))