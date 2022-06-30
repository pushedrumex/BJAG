from collections import deque

def change(s): # 올림(#)이 있다면 소문자로 변환 후 반환
    temp = deque(s)
    s = []
    while temp:
        if temp[0] == '#':
            temp.popleft()
            s[-1] = s[-1].lower()
        else:s.append(temp.popleft())
    return "".join(s)

def solution(m, mif):
    answer = ''
    d = []
    m = change(m)
    for i in range(len(mif)):
        temp = mif[i].split(',')
        temp[-1] = change(temp[-1])
        t =  60*(int(temp[1][:2])-int(temp[0][:2])) + int(temp[1][3:5])-int(temp[0][3:5])
        rep = temp[-1]*2 # 2번 반복했을 때의 악보
        if t<2*len(rep):temp[-1] = rep[:t] # 완벽하게 2번 반복을 안했다면
        else:temp[-1] *= len(m)//len(temp[-1]) + 2
        if m in temp[-1]:d.append([t,len(mif)-i,temp[-2]])
    if not d:
        return '(None)'
    d = sorted(d,reverse=True)
    return d[0][-1]
