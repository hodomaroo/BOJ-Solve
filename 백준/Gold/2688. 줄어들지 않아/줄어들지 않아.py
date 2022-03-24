dp = [[0] * 10 for _ in range(65)]
dp[0][0] = 1 #Base는 여기에서 시작한다.
for i in range(1,65):
    dp[i][0] = dp[i-1][0]
    for j in range(1,10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for i in range(int(input())):
    print(sum(dp[int(input())]))