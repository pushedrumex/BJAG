from collections import defaultdict

answers = []
dic1 = defaultdict(list)
dic2 = defaultdict(int)

def dfs(city, cities, cnt):
    global answers
    if cnt == 0:
        answers.append(cities)
        return
    for _city in dic1[city]:
        if dic2[city + _city] > 0:
            dic2[city + _city] -= 1
            dfs(_city, cities + [_city], cnt-1)
            dic2[city + _city] += 1
    
def solution(tickets):

    N = len(tickets)
    for a, b in tickets:
        dic1[a].append(b)
        dic2[a + b] += 1

    dfs("ICN", ["ICN"], N)

    return sorted(answers)[0]
