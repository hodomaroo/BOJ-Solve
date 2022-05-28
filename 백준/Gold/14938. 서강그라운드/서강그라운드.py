import heapq
inf = 10e9

def dijkstra(node):
    global M
    heap = [(0,node)]
    visit = [False for _ in range(1+N)]
    dp = [inf for _ in range(1 + N)]

    stack = []

    while heap:
        cost,node = heapq.heappop(heap)
        if visit[node]: continue
        stack.append(node)
        visit[node] = True


        for next_node,dist in graph[node]:
            next_cost = dist + cost

            if not visit[next_node] and next_cost < min(dp[next_node],M+1):
                dp[next_node] = next_cost
                heapq.heappush(heap,(next_cost,next_node))
    #print(stack)
    return sum([items[x] for x in stack])



N,M,R = list(map(int,input().split()))
items = [0] + list(map(int,input().split()))
#print(items)
graph = [[] for i in range(N+1)]

for i in range(R):
    f,t,cst = list(map(int, input().split()))

    graph[f].append((t, cst))
    graph[t].append((f, cst))

#print(graph)

sol = 0
for i in range(1,N+1):
    sol = max(sol,dijkstra(i))
print(sol)
