n = int(input())
nums = list(map(int,input().split()))
dp = [[0] * 21 for _ in range(2)] #0~21 Case 저장
dp[0][nums[0]] = 1
conv = 0

for v in nums[1:-1]:
    for i in range(21):
        if 0 <= i - v <= 20:
            dp[1 - conv][i - v] += dp[conv][i]
        if 0 <= i + v <= 20:
            dp[1 - conv][i + v] += dp[conv][i]

    dp[conv] = [0] * 21
    conv = 1 - conv

print(dp[conv][nums[-1]])