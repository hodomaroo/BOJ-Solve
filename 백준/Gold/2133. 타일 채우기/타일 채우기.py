import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
dp[0] = 1

if N >= 2:
    dp[2] = 3

if N >= 4:
    for i in range(4,N+1,2):
        dp[i] = dp[i - 2] * 3

        for j in range(i-4,-1,-2):
            dp[i] += 2 * dp[j]

print(dp[N])