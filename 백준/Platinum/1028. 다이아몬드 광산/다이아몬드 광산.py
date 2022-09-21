import sys

input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dp = [[[-1,-1] for _ in range(m + 2)] for _ in range(n + 2)]

ans = 0
for i in range(1,n + 1):
    for j in range(1, m + 1):
        if not board[i - 1][j - 1]: continue
        ans = max(ans,1)
        
        dp[i][j][0] = dp[i-1][j-1][0] + 1
        dp[i][j][1] = dp[i-1][j+1][1] + 1
        
        for s in range(min(dp[i][j]), ans -1, -1): 
            if dp[i - s][j - s][1] >= s and dp[i-s][j + s][0] >= s:
                ans = max(s + 1,ans)
                break      
print(ans)   