from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    
    #return CostTable
    def dijkstra(start : int) -> list:
        
        dp = [1000000 for _ in range(n + 1)] 
        visit = [False] * (n + 1)
        
        dp[start] = 0
        heap = [(0,start)]
        
        while heap:
            cost, node = heappop(heap)
            
            if visit[node]: continue
            visit[node] = True
            
            for nextnode,bill in graph[node]:
                if not visit[nextnode] and bill + cost < dp[nextnode]:
                    dp[nextnode] = bill + cost
                    heappush(heap,(dp[nextnode], nextnode))
        return dp
    
    graph = [[] for _ in range(n + 1)]
    
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    #print(graph)
    startCost = dijkstra(s)    
    aCost = dijkstra(a)    
    bCost = dijkstra(b)    
    #print(startCost,aCost,bCost)
    
    ans = float("inf")
    
    for i in range(1, n + 1):
        ans = min(ans, startCost[i] + aCost[i] + bCost[i])    
    
    return ans