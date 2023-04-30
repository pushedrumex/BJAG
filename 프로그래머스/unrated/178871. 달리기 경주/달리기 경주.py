def solution(players, callings):
    answer = []
    N = len(players)
    dic1 = {}
    dic2 = {}
    for i in range(1, N+1):
        dic1[i] = players[i-1]
        dic2[players[i-1]] = i
    for name in callings:
        rank = dic2[name]
        dic1[rank] = dic1[rank-1]
        dic2[dic1[rank]] = rank         
        dic1[rank-1] = name
        dic2[name] = rank-1
    for i in range(1, N+1):
        answer.append(dic1[i])
    
    return answer