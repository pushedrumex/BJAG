import math

def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    deploy = []
    for i in range(N):
        deploy.append(math.ceil((100-progresses[i])/speeds[i]))
    
    print(deploy)
    day = deploy[0]
    cnt = 0
    for i in range(N):
        if day >= deploy[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = deploy[i]
    answer.append(cnt)
    return answer