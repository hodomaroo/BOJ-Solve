import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
nodePos = [list(map(int,input().split())) for _ in range(n)]
graph = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        distance = sqrt(abs(nodePos[i][0] - nodePos[j][0]) ** 2 + abs(nodePos[i][1] - nodePos[j][1]) ** 2)
        graph[i][j] = distance
        graph[j][i] = distance

#i에서 시작하는 경우로 해서 다 돌리기
minCost = float("inf")
dp = [[-1] * pow(2, n) for _ in range(n)]  # node별로 2^n가지 상태가 존재
check = pow(2,n)-1
ans = float('inf')

#print(*graph,sep="\n")

def dfs(node, stat):
    if dp[node][stat] != -1: return dp[node][stat]

    if check == stat:
        return graph[node][0]

    dp[node][stat] = float("inf")

    for i in range(n):
        nextstat = stat | 1 << i
        if stat == nextstat: continue

        dp[node][stat] = min(dp[node][stat],dfs(i,nextstat) + graph[node][i])
    return dp[node][stat]
print(dfs(0,1))


