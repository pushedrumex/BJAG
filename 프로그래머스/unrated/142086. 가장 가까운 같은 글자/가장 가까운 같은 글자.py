from collections import defaultdict

def solution(s):
    dic = defaultdict(lambda: -1)
    answer = []
    for i in range(len(s)):
        c = s[i]
        if dic[c] > -1: answer.append(i-dic[s[i]])
        else: answer.append(-1)
        dic[s[i]] = i
    return answer