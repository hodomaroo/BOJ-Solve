n = int(input())
nums = list(map(int,input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = (dp[i] + dp[j]) % 998244353

print(*dp)