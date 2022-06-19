s = list(input())
stk = []
d = {'+':1,'-':1,'*':2,'/':2,'(':3}
for i in s:
    if i not in '+-*/()':print(i,end="")
    else:
        if i == ')':
            while stk[-1] != '(':print(stk.pop(),end="")
            stk.pop()
        elif not stk or d[i] > d[stk[-1]]:stk.append(i)
        else:
            while stk and stk[-1] != '(' and d[stk[-1]] >= d[i]:print(stk.pop(),end="")
            stk.append(i)
while stk:print(stk.pop(),end="")