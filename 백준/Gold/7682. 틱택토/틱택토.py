# X -> O -> X ...
# X-O == 0 또는 1개
# O가 성공했으면 X의 개수가 더 많으면 안됨
# X가 성공했으면 X-O == 1

while True:
    arr = input()
    if arr == "end":
        break
    arr = [arr[:3], arr[3:6], arr[6:]]

    x, o = 0, 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == "X":
                x += 1
            elif arr[i][j] == "O":
                o += 1
    
    x_bingo, o_bingo = 0, 0
    for row in arr:
        if row == "XXX":
            x_bingo += 1
        elif row == "OOO":
            o_bingo += 1
    
    for j in range(3):
        temp = ""
        for i in range(3):
            temp += arr[i][j]
        if temp == "XXX":
            x_bingo += 1
        elif temp == "OOO":
            o_bingo += 1

    i, j = 0, 0
    temp = ""
    for k in range(3):
        temp += arr[i+k][j+k]
    if temp == "XXX":
        x_bingo += 1
    elif temp == "OOO":
        o_bingo += 1

    temp = ""
    i, j = 0, 2
    for k in range(3):
        temp += arr[i+k][j-k]
    if temp == "XXX":
        x_bingo += 1
    elif temp == "OOO":
        o_bingo += 1
    
    if x < o:
        print("invalid")
        continue
    if x-o > 1:
        print("invalid")
        continue
    if x_bingo > 0 and x != o+1:
        print("invalid")
        continue
    if o_bingo > 0 and x != o:
        print("invalid")
        continue
    if (x_bingo + o_bingo) == 0 and x+o != 9:
        print("invalid")
        continue     

    print("valid")