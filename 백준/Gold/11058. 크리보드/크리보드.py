dp = [0] * 101
dp[0],dp[1],dp[2] = [0,1,2]

for i in range(3,101):
    dp[i] = dp[i-1] + 1

    for target in range(i-3,-1,-1):
        dp[i] = max(dp[i], dp[target] * (i - target - 1))
print(dp[int(input())])