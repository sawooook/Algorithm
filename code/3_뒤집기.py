import heapq

n,m = map(int, input().split())
temp = []
cards = []
temp.extend(input().split())
for i in temp:
    heapq.heappush(cards, int(i))
# 2 3 6
count = 0
while count != m:
    count += 1
    first_card = heapq.heappop(cards)
    second_card = heapq.heappop(cards)
    for i in range(2):
        heapq.heappush(cards, first_card + second_card)
print(sum(cards))