import sys

sys.setrecursionlimit(100010)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
pointDp = [0 for _ in range(n+1)]

for idx,value in enumerate(list(map(int,input().split()))):
    if value < 0: continue
    graph[value].append(idx+1)
for _ in range(m):
    i,w = map(int,input().split())
    pointDp[i] += w   #혹시 중복으로 들어올수도 있음

def dfs(node : int, parent : int) -> int:
    if parent > 0:
        pointDp[node] += pointDp[parent]

    for nextnode in graph[node]:
        dfs(nextnode,node)
dfs(1,-1)
print(*pointDp[1:])




