from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    #(cost , nodeValue)
    nodes = [float("inf") for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    
    for a,b,c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    heap = []
    for i in gates:
        nodes[i] = 0
        heappush(heap, (0,i))
    
    for i in summits:
        visit[i] = True

    while heap:
        cost, node = heappop(heap)
        if visit[node]: continue
        visit[node] = True
        
        for nextnode,nextcost in graph[node]:
            if nodes[nextnode] > max(cost, nextcost):
                nodes[nextnode] = max(cost, nextcost)
                heappush(heap, (nodes[nextnode], nextnode))
    
    ans = min(summits, key = lambda x : (nodes[x],x))
    return [ans,nodes[ans]]