def solution(citations):
    n = len(citations)
    citations.sort()
    answer = 0
    for i in range(n):
        h = citations[i]
        if n - i >= h:
            answer = h
        else:
            answer = max(answer, n - i)
            break
    return answer