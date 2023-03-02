from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while priorities:
        temp = priorities.popleft()
        location -= 1
        if priorities and max(priorities) > temp:
            priorities.append(temp)
            if location == -1: location = len(priorities)-1
        else:
            answer += 1
            if location == -1:
                return answer