import collections
a = [1,2]
b = [-2,-1]
c = [-1, 2]
d = [0, 2]
sum_ab = []
sum_cd = []
res = 0
dic = {}
for n1 in a:
    for n2 in b:
        tmp = n1 + n2
        if tmp in dic:
            dic[tmp] += 1
        else:
            dic[tmp] = 1

for n1 in c:
    for n2 in d:
        tmp = 0 - (n1 + n2)
        if tmp in dic:
            res += d[tmp]
print(res)

ab = [-1,1,0,1]
cd = [0,0,1,-1]
count = 0
for key in ab:
    if -key in cd:
        count += ab[key] * cd[-key]
print(count)

