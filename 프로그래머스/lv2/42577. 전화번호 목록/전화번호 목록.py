from collections import defaultdict

def solution(phone_book):
    d = defaultdict(bool)
    for n in phone_book:d[n] = True
    for n in phone_book:
        for i in range(1,len(n)):
            if d[n[:i]]:return False
    return True