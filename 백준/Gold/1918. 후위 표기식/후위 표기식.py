## 후위 표기식

s = list(input())
stk = []   # 연산자 스택
d = {'+':1,'-':1,'*':2,'/':2,'(':3}

for i in s:
    if i not in '+-*/()':print(i,end="")   # 연산자가 아니라면 출력
    else:
        if i == ')':
            while stk[-1] != '(':print(stk.pop(),end="")  # 열린괄호가 나올때까지 스택 print pop
            stk.pop()                                     # 열린괄호 pop

        elif not stk or d[i] > d[stk[-1]]:stk.append(i)   # 빈 스택이거나 top이 나보다 우선순위가 낮다면 append
        else:
            while stk and stk[-1] != '(' and d[stk[-1]] >= d[i]: print(stk.pop(),end="")
            # 열린괄호가 아니면서 나보다 우선순위가 높거나 같은것들 print pop
            stk.append(i)                                 # 마지막에 내 자신 append
while stk:print(stk.pop(),end="")  # 남은 연산자들 print pop
