def solution(food):
    answer = ''
    temp = []
    for i in range(1, len(food)):
        temp += [i] * (food[i] // 2)
    return "".join(map(str, temp + [0] + temp[::-1]))