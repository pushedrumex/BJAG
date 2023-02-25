def solution(keymap, targets):
    answer = []
    n = len(keymap)
    dic = {}
    for i in range(n):
        temp = list(keymap[i])
        for j in range(len(temp)):
            if temp[j] not in dic:
                dic[temp[j]] = j+1
            else:
                dic[temp[j]] = min(j+1, dic[temp[j]])
                
    for target in targets:
        cnt = 0
        for c in target:
            if c in dic: cnt += dic[c]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer