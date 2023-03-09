from heapq import heappush, heappop

# 첫번째로, 요청 시간 순으로 정렬
# 두번째로, 요청 시간이 가까운 작업이 실행되면 해당 작업의 요청시간 + 작업시간 >= 요청시간인 작업들을 대기큐에 작업시간 순으로 우선순위 큐 구성

def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort(reverse=True)
    readyQ = []
    
    while readyQ or jobs:
        if readyQ: time, req = heappop(readyQ)
        else:
            req, time = jobs.pop()
            current = req

        # 대기시간 + 작업시간
        answer += current - req + time
        current += time

        while jobs and jobs[-1][0] <= current:
            req_tmp, time_tmp = jobs.pop()
            heappush(readyQ, (time_tmp, req_tmp))

    return answer // N