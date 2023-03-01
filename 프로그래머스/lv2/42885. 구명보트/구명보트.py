from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while people:
        answer += 1
        heavy = people.pop()
        if people and heavy + people[0] <= limit:
            people.popleft()
    return answer