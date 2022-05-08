while True:
    stc = input()
    if stc[0] == '.':exit()
    result = 'yes'
    S = []
    L = []
    for i in range(len(stc)):
        if stc[i] == '.':break
        if stc[i] == '(':S.append(i)
        elif stc[i] == ')':
            if not S:result = 'no';break
            if L and L[-1] > S[-1]:result = 'no';break
            S.pop()
        elif stc[i] == '[':L.append(i)
        elif stc[i] == ']':
            if not L: result = 'no';break
            if S and S[-1] > L[-1]: result = 'no';break
            L.pop()

    if S or L:result = 'no'
    print(result)
