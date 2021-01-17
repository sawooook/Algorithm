#- leetcode(1009번)
N = 7
binary_n = bin(N)
change_n = ""
for i in binary_n[2:]:
    if i == "0":
        change_n += "1"
    elif i == "1":
        change_n += "0"

ans = int(change_n, 2)
print(ans)
#- bin 함수를 써서 2진수로 바꾼 다음 조건에 맞게 변경해줌
# 그다음 int함수를 이용해서 10진수로 바꿔줌
# 참고할것 bin 메서드를 사용할때 인풋은 int로
# int를 이용해서 10진수로 바꿔줄땐 str

#- 다른 사람풀이
# for문 말고 replace써도 좋을듯

