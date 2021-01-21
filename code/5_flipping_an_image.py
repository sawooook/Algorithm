input = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
flliped = []
result = []
for i in input:
    flliped.append(i[::-1])
for i in flliped:
    curr = []
    for k in i:
        if k == 0:
            curr.append(1)
        else:
            curr.append(0)
    result.append(curr)

#print(result)


## 결국 못풀어서 답안을 본문제,,,
#어차피 0이랑 1두개의 숫자만 있으니까 거꾸로 뒤집는다는 생각을 뒤로 넣는다고
# 생각하다니 진짜 똑똑하다 --> [::-1]

# 그리고 0하고 1이니 절대값을 이용해서 -1 해주는것도 진짜 똑똑한듯 ,,
