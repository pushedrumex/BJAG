from collections import defaultdict

def solution(want, number, discount):
    want_dic = defaultdict(int)
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
    
    answer = 0
    for i in range(len(discount)-9):
        discount_dic = defaultdict(int)
        for j in range(i, i+10):
            discount_dic[discount[j]] += 1
        flag = True
        for _good in want_dic.keys():
            if want_dic[_good] > discount_dic[_good]:
                flag = False
                break
                
        if flag:
            answer += 1

    return answer