from itertools import combinations
def solution(number):
    answer = 0
    for temp in list(combinations(number, 3)):
        if sum(temp) == 0:
            answer += 1
    return answer