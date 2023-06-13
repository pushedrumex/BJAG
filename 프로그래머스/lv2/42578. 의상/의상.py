from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1
    for key in dic.keys():
        answer *= dic[key] + 1
    return answer - 1