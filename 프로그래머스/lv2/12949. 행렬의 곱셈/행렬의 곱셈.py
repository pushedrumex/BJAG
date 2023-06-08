def solution(arr1, arr2):
    N1, N2 = len(arr1), len(arr2)
    M1, M2 = len(arr1[0]), len(arr2[0])

    answer = [[0] * M2 for _ in range(N1)]

    for i in range(N1):
        for j in range(M2):
            for k in range(M1):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer