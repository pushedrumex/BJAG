from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        words += set(product("AEIOU",repeat=i))
        
    words = sorted(list(words))
    for i in range(len(words)):
        if "".join(words[i]) == word:
            return i+1
    return -1