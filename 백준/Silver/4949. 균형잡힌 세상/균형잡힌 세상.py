d = {')':'(',']':'['}

while True:
    s = input()
    if s == '.':exit()
        
    flag = 0 # 올바른 문장이라면 0
    
    stack = []
    for c in s:
        if c in d.values():stack.append(c)
        elif c in d.keys():
            if not stack or stack.pop() != d[c]:flag=1;break
            # 닫는 괄호가 나왔을 때, stack에 저장된 열린괄호가 없거나 가장 최근에 append된 문자가 해당 열린 괄호가 아닐경우
                
    if stack:flag=1 # 괄호가 짝지어지지 않았을 경우
        
    if flag == 1:print('no')
    else:print('yes')
