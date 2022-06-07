from collections import deque

n = int(input())
distance = [0] * (n + 1)
isCycle = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = [v for v in range(1, n + 1) if len(graph[v]) == 1]
if not queue:
    print(*([0] * n))
    exit()

def findCycleDfs(node : int, par : int) -> int: #--> return cycleStartNode

    visit[node] = True
    target = 0

    for nextnode in graph[node]:
        if par == nextnode: continue
        if target: break
        target = max(target, nextnode if visit[nextnode] else findCycleDfs(nextnode, node))

    isCycle[node] = (target > 0)
    return target if target and target != node else 0


findCycleDfs(queue[0],-1)
visit = [isCycle[node] for node in range(n + 1)]
queue = deque(v for v in range(1, n + 1) if isCycle[v])

while queue:
    node = queue.popleft()

    for nextnode in graph[node]:
        if visit[nextnode]: continue
        visit[nextnode] = True
        distance[nextnode] = distance[node] + (1 - isCycle[nextnode])
        queue.append(nextnode)

print(*distance[1:])

