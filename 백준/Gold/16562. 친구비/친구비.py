import sys
sys.setrecursionlimit(10**5)
#노드군집 disjoint Set

n,m,k = map(int,input().split())
cost = list(map(int,input().split()))
graph = [[] for _ in range(n)]
visit = [False] * n
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    graph[a].append(b)
    graph[b].append(a)

def dfs(node : int) -> int:
    visit[node] = True
    bill = cost[node]

    for nextnode in graph[node]:
        if visit[nextnode]: continue
        bill = min(bill, dfs(nextnode))
    return bill

ans = 0
for i in range(n):
    if visit[i]:continue
    ans += dfs(i)
print(ans if k >= ans else "Oh no")