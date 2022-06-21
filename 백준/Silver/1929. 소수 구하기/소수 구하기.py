M, N = map(int, input().split())
root = int(N ** 0.5)

prime = [True] * (N + 1)   # prime = [True, True, True, True, True... ] (N+1)개
prime[0] = False           #            0     1     2     3    4
prime[1] = False
# prime = [False, False, True, True ... ]

for i in range(2, root + 1): # 2 ~ root, root까지만 검사해도 소수가 아닌것들은 다 False가 됨
    if prime[i] == True:   # 검사할 것들 중 가장 작은 소수
        for j in range(2*i, N + 1, i): # N까지 i(소수)의 배수인 것들은 False
            prime[j] = False

for i in range(M, N+1):
    if prime[i] == True:
        print(i)
        
        
# 비슷한 풀이 : 시간이 더 오래걸림
# 1부터 n까지 있는 소수 개수 

def solution(n):
    num=set(range(2,n+1)) # set은 뺄셈 가능

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
