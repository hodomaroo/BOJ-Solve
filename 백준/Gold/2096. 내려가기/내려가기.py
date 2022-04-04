n = int(input())
table = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0,0] for _ in range(3)] for _ in range(2)] #max/min

for i in range(3):  dp[1][i] = [0,0]

indexTable = [(0,1),(0,1,2),(1,2)]

maxAns,minAns = -float("inf"),float("inf")
for i in range(n):

    for j in range(3):
        dp[i % 2][j][0] = table[i][j] + max(dp[not i % 2][_][0] for _ in indexTable[j])
        dp[i % 2][j][1] = table[i][j] + min(dp[not i % 2][_][1] for _ in indexTable[j])

        if i == n-1:
            maxAns = max(maxAns, dp[i % 2][j][0])
            minAns = min(minAns, dp[i % 2][j][1])
print(maxAns,minAns)





