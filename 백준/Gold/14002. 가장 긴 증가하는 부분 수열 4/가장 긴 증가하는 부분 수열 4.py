n = int(input())
nums = list(map(int,input().split()))
dp = [1] * (n)

maxLen = 1
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i],dp[j] + 1)
            maxLen = max(dp[i],maxLen)

#print(dp) # --> N으로 그대로 역추적

stack = []
for i in range(n-1,-1,-1):
    if dp[i] == maxLen:
        stack.append(nums[i])
        maxLen -= 1
print(len(stack))
print(*stack[::-1])