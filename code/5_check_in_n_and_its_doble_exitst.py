#- leetcode(1346번)
arr = [-20,8,-6,-14,0,-19,14,4]

if 0 in arr:
    if arr.count(0) > 1:
        print("true")
    else:
        arr.pop(arr.index(0))
for a in arr:
    if (a * 2) in arr:
        print("TRUE")
else:
    print("FALSE")

#- 다른사람들 풀이
# set을 만들어준다음 곱한값과 나눈값을 넣어서 확인
# 굿아이디어!
s = set()
for num in arr:
    if num not in s:
        if num % 2 == 0:
            s.add(num//2)
        s.add(num*2)
    else:
        print("TRUE")
else:
    print("FALSE")