n = 5
m = 8
k = 3

list = [2,4,5,4,6]
sorted_reverse_list = sorted(list, reverse=True)
count = 0
result = 0
while m != 0:
    if count == k:
        count = 0
        result += sorted_reverse_list[1]
    else:
        count +=1
        result += sorted_reverse_list[0]
    m -= 1
print(result)





n = 5
m = 8
k = 3

list = [2,4,4,4,4]
sorted_list = sorted(list)
result = 0
first_num = sorted_list[-1]
second_num = sorted_list[-2]

sorted_list = list
# [6,6,6,5,6,6,6,5]
second_count = (m//(k+1))
first_count = m - second_count
result += (first_num * first_count)
result += (second_num * second_count)
print(result)

# 1번 같이 풀게 되면 count 가 100만 이상이면 너무 오래걸려서 타임아웃 에러가 발생할 수 있음
# 그래서 2번같이 풀면좋음 규칙을 찾아서 풀어보자