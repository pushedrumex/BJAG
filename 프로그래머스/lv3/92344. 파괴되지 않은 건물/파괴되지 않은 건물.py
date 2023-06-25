def solution(board, skill):
    N = len(board)
    M = len(board[0])
    
    record = [[0] * (M+2) for _ in range(N+2)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        record[r1+1][c1+1] += degree
        record[r2+2][c2+2] += degree
        record[r1+1][c2+2] -= degree
        record[r2+2][c1+1] -= degree

    # 누적합
    for i in range(1, N+1):
        for j in range(1, M+1):
            record[i][j] += record[i-1][j] + record[i][j-1] - record[i-1][j-1]            
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + record[i+1][j+1]> 0:
                answer += 1
    
    return answer