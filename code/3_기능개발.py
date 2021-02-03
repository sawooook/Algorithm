n = [1,1,9,1,1]
location = 0
first_paper = n[0]
count = 1
while n:
    max_paper = max(n)
    if n[0] != max_paper:
        out_num = n.pop(0)
        n.append(out_num)
        if location == 0:
            location = len(n)-1
        else:
            location -= 1
    elif n[0] == max_paper:
        count += 1
        if location == 0:
            print(count)
            break
        else:
            n.pop(0)
            if location == 0:
                location = len(n) - 1
            else:
                location -= 1
