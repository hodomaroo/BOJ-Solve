import sys
input = sys.stdin.readline
N = int(input())
ns = [0]
ns.extend([int(input()) for _ in range(N)])
dp = [0 for _ in range(N+1)]

if N >= 1:
    dp[1] = ns[1]
if N >= 2:
    dp[2] = ns[2] + ns[1]
if N >= 3:
    for i in range(3,N+1):
        dp[i] = max(dp[i-1],dp[i-2]+ns[i],dp[i-3]+ns[i]+ns[i-1])
print(dp[-1])


