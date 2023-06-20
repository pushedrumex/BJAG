from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)
    answer = 0
    
    for order in permutations(dungeons, N):
        _k = k
        cnt = 0
        for a, b in order:
            if _k >= a:
                _k -= b
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    return answer