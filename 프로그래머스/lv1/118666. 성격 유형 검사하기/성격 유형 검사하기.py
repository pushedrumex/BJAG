from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dic = defaultdict(int)
    for i in range(len(survey)):
        type, choice = survey[i], choices[i]
        if choice < 4:
            dic[type[0]] += 4 - choice
        elif choice > 4:
            dic[type[1]] += choice - 4
    for type in ["RT", "CF", "JM", "AN"]:
        if dic[type[1]] > dic[type[0]]: answer += type[1]
        else: answer += type[0]
    return answer