s = "abcabcbb"
text = ""
result = 0
# abc
for i in s:
    if i not in text:
        text += i
    else:
        text = text[text.index(i)+1:] + i
    result = max(result, len(text))

print(result)

# 이런문제일 경우에는 ,, TEXT라는거에다가 계속 집어넣고 만약 중복문자가 나오면 맨앞문자를 지워주고 계속 넣자
