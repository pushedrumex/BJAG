from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapify(scoville)
    mix = 0
    while len(scoville) > 1 and scoville[0] < K:
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + b * 2)
        mix += 1
    if scoville[0] >= K: return mix
    else: return -1