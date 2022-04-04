def star(N, d, k):
    temp = d[:]
    if N == 3:
        for i in d:
            for j in i:
                print(j, end="")
            print()
    else:
        for i in range(len(temp) * 2):
            d.append([])
        n = len(d)//3
        for i in range(len(d)):
            d[i] = temp[i%(k)] * 3
        for i in range(len(d)):
            for j in range(len(d)):
                if n <= j < n * 2 and  n <= i < n * 2:
                    d[i][j] = " "
        k *= 3
        star(N//3, d, k)
d = [["*","*","*"],["*"," ","*"],["*","*","*"]]
star(int(input()), d, 3)