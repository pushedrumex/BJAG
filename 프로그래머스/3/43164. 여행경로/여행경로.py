from collections import defaultdict, deque

answer = []
spots = []
graph = defaultdict(list)
visited = defaultdict(int)
ticket_count = None
def dfs(a, count):
    global answer
    
    if count == ticket_count:
        if len(answer) == 0:
            answer = spots[:]
        else:
            answer = min(answer, spots[:])
        return
    
    for b in graph[a]:
        if visited[(a, b)] <= 0: continue
        visited[(a, b)] -= 1
        spots.append(b)
        
        dfs(b, count + 1)
        
        visited[(a, b)] += 1
        spots.pop()
        
def solution(tickets):
    global ticket_count
    
    ticket_count = len(tickets)
    for a, b in tickets:
        graph[a].append(b)
        visited[(a, b)] += 1
    
    for a in graph.keys():
        graph[a].sort()
        
    start = "ICN"
    spots.append(start)
    
    dfs(start, 0)
    
    return answer