import sys
input = sys.stdin.readline
n = int(input())
dp = [[float("inf")] * n for _ in range(n)]

for i in range(int(input())):
    s,e,c = map(int,input().split())
    dp[s-1][e-1] = min(dp[s-1][e-1],c)

for i in range(n):
    dp[i][i] = 0


for bet in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][bet] + dp[bet][j],dp[i][j])


for v in dp:
    for vv in v:
        print(vv if 0 < vv < float("inf") else 0,end=" ")
    print()




