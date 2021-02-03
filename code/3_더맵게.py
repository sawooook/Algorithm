graph = []
for i in range(4):
    graph.append(list(map(int, input().split())))

que = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
que.append([0, 0])
while que:
    x, y = que.pop(0)

    if x == 3 and y == 3:
        print(graph)
        break

    for i in range(4):
        move_x = dx[i] + x
        move_y = dy[i] + y
        if move_x >= 0 and move_y >= 0 and move_x <= 3 and move_y <= 3:
            if graph[move_x][move_y] == 1:
                graph[move_x][move_y] = 2
                que.append([move_x, move_y])