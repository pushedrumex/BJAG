from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(lambda : [0, defaultdict(int)])
    for i in range(len(genres)):
        dic[genres[i]][0] += plays[i]
        dic[genres[i]][1][i] += plays[i]
    answer = []
    for genre, sing in sorted(dic.items(), key=lambda item: item[1], reverse=True):
        temp = sorted(sing[1].items(), key=lambda item : item[1], reverse=True)[:2]
        answer += [i[0] for i in temp]
    return answer