#- leetcode(202번)
n = 19
str_n = str(n)
result = []
while n != 1:
    if n in result:
        print("FALSE")
        break
    result.append(n)
    str_n = str(n)
    n = 0
    for i in str_n:
        n += (int(i)**2)
else:
    print("TRUE")

#- 이 문제의 경우 무한 반복으로 숫자가 돌아가는 문제기 때문에 무한루프에
# 걸릴수 있다. 그러므로 배열 같은걸 만들어서 무한루프에서 탈출하도록 하는것도 좋은방법같다

# 다른 사람들 풀이
n = 7
s = set()
while n != 1:
    sum_num = sum([int(i) ** 2 for i in str(n)])
    if s in sum_num:
        print("FALSE")
    else:
        s.add(sum_num)
else:
    print("TRUE")