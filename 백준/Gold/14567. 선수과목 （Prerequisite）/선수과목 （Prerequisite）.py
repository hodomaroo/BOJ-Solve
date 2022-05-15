import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1) #indegree가 0인 애로 시작
dp = [0] * (n + 1)

def dfs(node : int) -> int:
    if dp[node]: return dp[node]

    for nextnode in graph[node]:
        dp[node] = max(dp[node],dfs(nextnode)+1)

    dp[node] = max(dp[node],1)
    return dp[node]

for i in range(m):
    f,t = map(int,input().split())
    graph[t].append(f) #t를 더 먼저
    indegree[f] += 1

ans = 0
for i in range(1,n+1):
    if not indegree[i]: dfs(i)

print(*dp[1:])



