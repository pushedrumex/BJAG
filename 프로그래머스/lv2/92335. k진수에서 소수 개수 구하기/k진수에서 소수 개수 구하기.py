def solution(n, k):
    
    k_base_num = ""
    
    while n:
        k_base_num = str(n % k) + k_base_num
        n //= k
    
    arr = k_base_num.split("0")
    answer = 0
    for n in arr:
        if not n: continue
        if is_prime(int(n)): answer += 1

    return answer

def is_prime(n):
    print(n)
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True