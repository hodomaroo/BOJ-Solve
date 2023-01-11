for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            dp[j] = (dp[j] + dp[j - i]) % 100999
    print(dp[n])