import sys
input = sys.stdin.readline

from heapq import heappop,heappush

n,m,a,b,c = map(int,input().rstrip().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    f,t,cost = map(int,input().rstrip().split())
    graph[f].append((t,cost))
    graph[t].append((f,cost))

def dijkstra(node,target):
    heap = []
    minShame = [[float("inf"), float("inf")] for _ in range(n + 1)]

    heappush(heap,(0,0,node))   #현재 노드 / 수치심 / 사용 비용
    minShame[node] = [0,0]

    while heap:
        shame,cost,node = heappop(heap)
        if [shame,cost] > minShame[node]: continue
        if node == target:
            print(shame)
            exit()

        for nextnode,nextcost in graph[node]:
            resultShame = max(shame,nextcost)
            resultCost = cost + nextcost

            if resultCost > c or [resultShame,resultCost] >= minShame[nextnode]: continue

            minShame[nextnode] = [resultShame,resultCost]
            heappush(heap,(resultShame,resultCost,nextnode))
dijkstra(a,b)
print(-1)