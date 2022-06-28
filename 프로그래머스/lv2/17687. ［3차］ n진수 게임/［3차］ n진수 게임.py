def solution(n, t, m, p):
    answer = ''
    nums = '0'
    base = '0123456789ABCDEF'
    for k in range(0,m*t):
        temp = []
        while k>0:
            temp.append(base[k%n])
            k //= n
        temp.reverse()
        nums += "".join(temp)
    for i in range(t):answer += nums[m*i+p-1]
    return answer
