import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m,q = map(int,input().split())
dp = [1 for i in range(n+1)]
visit =[False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    f,t = map(int,input().split())
    graph[f].append(t)
    graph[t].append(f)

def dfs(node : int) -> int:
    visit[node] = True
    for nextnode in graph[node]:
        if visit[nextnode]: continue
        dp[node] += dfs(nextnode)
    return dp[node]

dfs(m)

for _ in range(q):
    print(dp[int(input())])
