from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    
    while section:
        left = section.popleft()
        while section and section[0]-left+1 <= m:
            right = section.popleft()
        answer += 1
    return answer