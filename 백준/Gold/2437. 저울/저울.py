N = int(input())
W = [int(i) for i in input().split()]

W.sort() # 1 1 2 3 6 7 30

target = 1
# [0 target]
for i in W:
    # i : 추가되는 무게, [i target + i] : 추가되었을 때 가능한 범위
    if target >= i:target += i 
    # target과 i가 겹쳐진다면 [0 target + i]로 퉁칠 수 있음
    # [0 target] [i target + i] -> [0 target + i]
    else:break
    # 퉁칠 수 없다면 빈공간 발생
print(target)

# 참고 : https://aerocode.net/392
