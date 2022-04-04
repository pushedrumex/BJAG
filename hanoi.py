## 하노이탑 쌓기

def hanoi_tower(N, start, end) :
    if N == 1 :
        print(start, end)
        return
       
    hanoi_tower(N-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(N-1, 6-start-end, end) # 3단계
    
N = int(input())
print(2**N-1)
hanoi_tower(N, 1, 3)
