user_input = list(map(str, input()))
arr = []
opened = ["[", "(", "{"]
closed = ["]", ")", "}"]

for i in user_input:
    if i in opened:
        arr.append(i)
    else:
        if len(arr) < 1:
            print(False)
            break

        if opened.index(arr[-1]) == closed.index(i):
            arr.pop()
        else:
            print(False)
            break
else:
    if not arr:
        print(True)
    else:
        print(False)