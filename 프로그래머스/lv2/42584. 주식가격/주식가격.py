from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        now = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if price < now:
                break
        answer.append(cnt)
    return answer