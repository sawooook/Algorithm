#- hakerRankvowels = ["A", "E", "I", "O", "U"]s = "BANANA"result = [0, 0]for i in range(len(s)):    print(s[i])    if s[i] in vowels:        result[1] += (len(s) - i)    else:        result[0] += (len(s) - i)if result[0] > result[1]:    print("Stuart ", result[0])elif result[0] < result[1]:    print("Kevin", result[1])else:    print("DRAW")#- 나는 이문제 포문을 처음부터 끝까지 돌리는 방식으로 했는데# 그렇게 하니까 시간초과가 나왔음# 근데 지금다시보니 어차피 처음시작이 모음이면 뒤에 모든 글자수만큼은# 모음임 그걸 이용하자#- 다시한번 무조건 포문부터 돌리자는 생각 x