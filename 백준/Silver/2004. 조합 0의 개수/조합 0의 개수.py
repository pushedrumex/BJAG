n,m=map(int,input().split())
def cntTwo(n):
    k = 2
    count = 0
    while k<=n: 
        count+=n//k
        k*=2
    return count
def cntFive(n):
    k = 5
    count = 0
    while k<=n: 
        count+=n//k
        k*=5
    return count
print(min(cntTwo(n)-cntTwo(m)-cntTwo(n-m),cntFive(n)-cntFive(m)-cntFive(n-m)))