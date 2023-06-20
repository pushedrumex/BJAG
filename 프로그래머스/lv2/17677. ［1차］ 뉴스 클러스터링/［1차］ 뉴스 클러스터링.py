import math
from collections import defaultdict

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    dic = defaultdict(int)

    union, intersection = 0, 0
    for i in range(len(str1)-1):
        word = str1[i:i+2]
        if word.isalpha():
            union += 1
            dic[word] += 1

    for i in range(len(str2)-1):
        word = str2[i:i+2]
        if word.isalpha():
            if dic[word] > 0:
                dic[word] -= 1
                intersection += 1
            else: union += 1
            
    if union == 0: return 65536

    return math.floor(intersection / union * 65536)