import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
costTable = [list(map(int,input().split())) for _ in range(n)]

#i에서 시작하는 경우로 해서 다 돌리기
minCost = float("inf")
dp = [[-1] * pow(2, n) for _ in range(n)]  # node별로 2^n가지 상태가 존재
check = pow(2,n)-1
ans = float('inf')

def dfs(node, stat):
    if dp[node][stat] != -1: return dp[node][stat]

    if check == stat:
        return costTable[node][0] if costTable[node][0] else float("inf")
        

    dp[node][stat] = float("inf")

    for i in range(n):
        nextstat = stat | 1 << i
        if stat == nextstat or costTable[node][i] == 0: continue

        dp[node][stat] = min(dp[node][stat],dfs(i,nextstat) + costTable[node][i])
    return dp[node][stat]
print(dfs(0,1))


