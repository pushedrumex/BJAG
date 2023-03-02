from collections import deque

def solution(priorities, location):
    answer = 0
    priority_table = [0]*10
    for p in priorities:
        priority_table[p] += 1
    priorities = deque(priorities)
    while priorities:
        temp = priorities.popleft()
        location -= 1
        if sum(priority_table[temp+1:]):
            priorities.append(temp)
            if location == -1: location = len(priorities)-1
        else:
            priority_table[temp] -= 1
            answer += 1
            if location == -1:
                return answer