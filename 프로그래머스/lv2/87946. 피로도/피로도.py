from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dungeon in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for a, b in dungeon:
            if a <= temp:
                count += 1
                temp -= b
            else:
                flag = False
                break
        answer = max(answer, count)
    return answer