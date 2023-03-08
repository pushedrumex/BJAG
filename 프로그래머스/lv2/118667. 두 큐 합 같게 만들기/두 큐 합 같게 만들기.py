from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 != 0: return -1
    max_cnt = len(queue1)*4
    queue1, queue2 = deque(queue1), deque(queue2)
    while answer < max_cnt and queue1 and queue2 and sum1 != sum2:
        answer += 1
        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum2 += num
            sum1 -= num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
    return answer if sum1 == sum2 else -1