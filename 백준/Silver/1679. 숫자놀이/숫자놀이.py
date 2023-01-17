n = int(input())
nums = list(map(int, input().split()))
dp = [[False] * 1001 for _ in range(int(input()) + 1)]
dp[0][0] = True

for i in range(1, len(dp)):
    for v in nums:
        for k in range(v, 1001):
            dp[i][k] = dp[i-1][k-v] | dp[i][k]

dp = [sum(dp[i][j] for i in range(len(dp))) > 0 for j in range(1001)]
print(f"{['holsoon', 'jjaksoon'][dp.index(False) % 2]} win at {dp.index(False)}")
    
    
