#- 프로그래머스(피보나치)
import sys
sys.setrecursionlimit(int(1e9))
dic = {}
def febo(n):
    if n in dic:
        return dic[n]

    if n == 0:
        dic[0] = 0
        return 0
    elif n == 1:
        dic[1] = 1
        return 1
    else:
        dic[n] = febo(n-1) + febo(n-2)
        return dic[n]
print(febo(100000))