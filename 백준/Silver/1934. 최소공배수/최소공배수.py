## 최대공약수를 구해서 나누기

import sys
T = int(input())
for i in range(T):
    A,B=map(int,sys.stdin.readline().rstrip().split())
    mul=A*B
    while A%B!=0:A,B=B,A%B
    print(mul//B)
