#- hackerRank
from collections import OrderedDict
alphabet = "AABCAAADA"
k = 3
split_size = len(alphabet)//k
s = []

for i in range(0, len(alphabet), k):
    print("".join(dict.fromkeys(alphabet[i:i+k])))

# set을 쓰면 정렬이 뒤죽박죽이므로
# 그럴땐 .join(dict.fromkey())를 사용할것
# 그리고 포문에서 맨뒤에 숫자를 넣으면 배수로 자름
# 3을 넣으면 3자리씩 자름