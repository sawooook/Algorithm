from collections import deque
nn = 4

out = str(nn)
funs = deque(["*", "//", "+", "-"])
for i in range(nn-1, 0, -1):
    out += funs[0] + str(i)
    funs.rotate(-1)
print(out)
print(eval(out))

# eval이란걸 통해서 문자를 계산할 수 있다는걸 알았음
# deque는 rotate기능이있음