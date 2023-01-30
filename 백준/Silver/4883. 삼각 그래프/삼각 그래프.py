count = 1

while True:
    
    n = int(input())
    if not n:   break
    
    dp = [list(map(int, input().split())) for _ in range(n)]    
    dp[0][0] = dp[-1][-1] = float("inf")
    for i in range(n):
        for j in range(3):
            if not i and j < 2: continue
            dp[i][j] = min(dp[i-1][j-1] if (i and j) else float("inf"),dp[i][j-1] if j else float("inf"),dp[i-1][j] if i else float("inf"),dp[i-1][j+1] if (i and j < 2) else float("inf")) + dp[i][j]

    print(f'{count}. {dp[-1][1]}')
    count += 1