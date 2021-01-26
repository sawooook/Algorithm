path = "NNSWWEWSSESSWENNW"
x = [0, 0, 1, -1]
y = [1, -1, 0, 0]
#    n  S  E  W
location = [0,0]
start = [0,0]
for i in path:
    if i == "N":
        start[0] = start[0] + x[0]
        start[1] = start[1] + y[0]
    elif i == "S":
        start[0] = start[0] + x[1]
        start[1] = start[1] + y[1]
    elif i == "E":
        start[0] = start[0] + x[2]
        start[1] = start[1] + y[2]
    elif i == "W":
        start[0] = start[0] + x[3]
        start[1] = start[1] + y[3]
    if start == location:
        print("True")
        break
else:
    print("FALSE")
