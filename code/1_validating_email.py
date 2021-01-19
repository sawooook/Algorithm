from itertools import groupby
s = "1222311"
result = []

for k, c in groupby(s):
    result.append((len(list(c)),int(k)))
print(result)

# 연속된숫자 묶어서 할때는 group_by쓰면 좋을거같음