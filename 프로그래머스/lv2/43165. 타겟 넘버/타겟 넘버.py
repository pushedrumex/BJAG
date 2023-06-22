answer = 0

def solution(numbers, target):
    dfs(0, numbers, 0, target)
    return answer

def dfs(i, numbers, n, target):
    global answer
    if i == len(numbers):
        if n == target:
            answer += 1
        return
    
    dfs(i+1, numbers, n-numbers[i], target)
    dfs(i+1, numbers, n+numbers[i], target)