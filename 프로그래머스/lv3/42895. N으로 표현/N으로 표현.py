# N은 1~8번 사용 가능
# 더하기, 빼기, 곱하기, 나누기, NNNNN ...

def solution(N, number):
    dp = [[] for _ in range(9)]
    for i in range(1, 9):
        dp[i].append(int(str(N)*i))
        if dp[i][0] == number: return i
        
        for j in range(1, i):
            
            for n1 in dp[j]:
                for n2 in dp[i-j]:
                    temp = [n1 + n2, n1 - n2, n1 * n2]
                    if n2 != 0: temp.append(n1 // n2)
                    for target in temp:
                        if target == number: return i
                    dp[i] += temp

    return -1