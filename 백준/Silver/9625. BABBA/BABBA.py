n = int(input())
#초기값은 A

dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 1

"""
Bottom Up
for i in range(1,n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = sum(dp[i - 1])
print(*dp[i])
"""
#"""
def TopDown(n):
    if n == 0: return [1,0]
    v1,v2 = TopDown(n-1)

    dp[n][0] = v2
    dp[n][1] = v1 + v2
    return dp[n]
#"""
print(*TopDown(n))