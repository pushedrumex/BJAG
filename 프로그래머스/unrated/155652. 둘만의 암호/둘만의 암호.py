from collections import defaultdict

def solution(s, skip, index):
    answer = ''
    dic = defaultdict(bool)
    for c in skip: dic[c] = True
    for c in s:
        cnt = 1
        temp_index = index
        while temp_index >= cnt:
            temp = (ord(c) - ord("a") + cnt) % 26
            if dic[chr(ord("a") + temp)]: temp_index += 1
            cnt += 1
        answer += chr(ord("a")+temp)
    return answer