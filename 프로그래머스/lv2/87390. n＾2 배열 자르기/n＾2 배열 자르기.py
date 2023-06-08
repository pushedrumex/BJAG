def solution(n, left, right):
    # graph = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(i+1):
    #         graph[j][i] = i+1
    #         graph[i][j] = i+1

#     temp = []
#     for row in graph:
#         temp += row
        
#     return temp[left:right+1]
    answer = []
    
    x, y = left // n, left % n
    end_x, end_y = right // n, right % n
    end_y += 1
    if end_y == n:
        end_x += 1
        end_y = 0
    while [x, y] != [end_x, end_y]:
        answer.append(max(x, y) + 1)
        y += 1
        if y == n:
            x += 1
            y = 0

    return answer
    