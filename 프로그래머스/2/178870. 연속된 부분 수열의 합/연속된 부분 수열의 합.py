def solution(sequence, k):
    answer = []
    N = len(sequence)
    
    if k == sequence[0]:
        return [0, 0]
    
    min_length = len(sequence) + 1
    left, right = 0, 1
    value = sequence[0] + sequence[1]
    while right < N and left <= right:
        if value <= k:
            if value == k and right - left + 1 < min_length:
                min_length = right - left + 1
                answer = [left, right]
            if right == N-1:
                break
            right += 1
            value += sequence[right]
        else:
            value -= sequence[left]
            left += 1
        
    return answer