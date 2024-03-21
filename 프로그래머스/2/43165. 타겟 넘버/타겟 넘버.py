answer = 0
def dfs(n, numbers, target):
    global answer
    
    if len(numbers) == 0:
        if n == target:
            answer += 1
        return
    
    x = numbers.pop()
    dfs(n+x, numbers, target)
    numbers.append(x)
    
    x = numbers.pop()
    dfs(n-x, numbers, target)
    numbers.append(x)
    

def solution(numbers, target):
    global q
    dfs(0, numbers, target)
    
    return answer