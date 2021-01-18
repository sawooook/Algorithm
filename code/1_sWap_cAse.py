s = "Www.HackerRank.com"
alphphet_big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"
                , "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphphet_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"
                  ,"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
result = ""
for alphabet in list(s):
    if alphabet in alphphet_big:
        result += alphabet.lower()
    elif alphabet in alphphet_small:
        result += alphabet.upper()
    else:
        result += alphabet
print(result)

#- 다른사람들 풀이 굳이 array에 넣지말고
for alphabet in list(s):
    if alphabet.upper():
        alphabet.lower()
    elif alphabet.lower():
        alphabet.upper()
# 이런식으로 해도 되고
# 아니면 swapcase() 메소드를 사용하면 바꿔줌
