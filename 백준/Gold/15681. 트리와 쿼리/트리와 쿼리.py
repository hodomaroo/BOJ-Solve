import sys
sys.setrecursionlimit(10**5 + 1)
input = sys.stdin.readline

n,m,q = map(int,input().rstrip().split())
dp = [1 for i in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    f,t = map(int,input().rstrip().split())
    graph[f].append(t)
    graph[t].append(f)

def dfs(parent : int, node : int) -> int:
    for nextnode in graph[node]:
        if nextnode == parent: continue
        dp[node] += dfs(node, nextnode)
    return dp[node]

dfs(-1,m)

for _ in range(q):
    print(dp[int(input().rstrip())])
