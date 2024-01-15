from itertools import permutations, product
from collections import defaultdict

def solution(dice):
    N = len(dice)
    max_count = 0
    answer = []
    visited = defaultdict(bool)
    for dices in permutations(range(N), N):
        A = tuple(sorted(dices[:N//2]))
        B = tuple(sorted(dices[N//2:]))
        
        if visited[A] or visited[B]:continue
        
        visited[A], visited[B] = True, True
        A_dice, B_dice = [], []
        for i in range(N // 2):
            A_dice.append(dice[A[i]])
            B_dice.append(dice[B[i]])

        A_sum, B_sum = [], []
        for nums in product(*A_dice):
            A_sum.append(sum(nums))
        for nums in product(*B_dice):
            B_sum.append(sum(nums))
        
        A_sum.sort()
        B_sum.sort()
        
        A_count, B_count = 0, 0
        for A_score in A_sum:
            A_count += bs(A_score, B_sum)
        for B_score in B_sum:
            B_count += bs(B_score, A_sum)
        
        if A_count > max_count:
            answer = A
            max_count = A_count
        if B_count > max_count:
            answer = B
            max_count = B_count

    answer = list(answer)
    for i in range(N // 2):
        answer[i] += 1

    return answer

def bs(score, sums):
    left, right = 0, len(sums) - 1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if sums[mid] < score:
            result = mid + 1
            left = mid + 1
        else:
            right = mid - 1
            
    return result
    