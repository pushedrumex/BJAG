def solution(e, starts):
    count = [0] * (e+1)
    for i in range(1, e+1):
        count[i] = get_count(i)

    max_n = e
    max_count = count[e]
    count[e] = max_n
    for i in range(e-1, 0, -1):
        c = count[i]
        if c >= max_count:
            max_count = c
            max_n = i
        count[i] = max_n

    answer = []
    for start in starts:
        answer.append(count[start])

    return answer

def get_count(n):
    root = int(n ** 0.5)
    result = 0
    for i in range(1, root+1):
        if n % i != 0: continue
        if i ** 2 == n:
            result += 1
        else:
            result += 2
    return result
    