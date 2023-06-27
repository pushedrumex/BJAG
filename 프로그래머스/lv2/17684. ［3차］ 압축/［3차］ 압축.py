from collections import deque

def solution(msg):
    idx = 1
    dic = {}
    
    for _ in range(26):
        dic[chr(ord("A") + idx - 1)] = idx
        idx += 1

    q = deque(list(msg))

    answer = []
    while q:
        temp = q.popleft()
        
        while q and temp in dic:
            temp += q.popleft()

        if temp in dic:
            answer.append(dic[temp])
        else:
            answer.append(dic[temp[:-1]])
            dic[temp] = idx
            idx += 1
            q.appendleft(temp[-1])

    return answer