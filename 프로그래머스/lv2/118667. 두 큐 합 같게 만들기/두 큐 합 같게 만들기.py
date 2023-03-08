from collections import deque
def solution(queue1, queue2):
    answer = -1
    allsum=sum(queue1)+sum(queue2)
    target=allsum/2
    q1=deque(queue1)
    q2=deque(queue2)
    lsum=sum(q1)
    
    cnt=0
    
    if max(q1)>target or max(q2)>target :
        return -1
    
    while q1 and q2 :
        if lsum>target :
            lsum-=q1.popleft()
            cnt+=1   
        elif lsum<target :
            tmp=q2.popleft()
            q1.append(tmp)
            lsum+=tmp
            cnt+=1 
        elif lsum==target :
            return cnt
    return answer