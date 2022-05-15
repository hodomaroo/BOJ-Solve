from collections import deque
SIZE = 100001
n,m = map(int,input().split())
dp = [float("inf")] * SIZE
count = [False] * SIZE

queue = deque([n])
dp[n] = 0
count[n] = 1
while queue:
    pos = queue.popleft()

    for nextpos in [pos - 1, pos + 1, pos * 2]:
        if not(0 <= nextpos < SIZE) or dp[nextpos] <= dp[pos]: continue

        if dp[nextpos] == float("inf"):
            queue.append(nextpos)
            dp[nextpos] = dp[pos] + 1
        count[nextpos] += count[pos]

print(dp[m])
print(count[m])