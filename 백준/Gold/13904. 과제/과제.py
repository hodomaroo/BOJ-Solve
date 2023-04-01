points = sorted([list(map(int, input().split()))
                for _ in range(int(input()))], key=lambda x: x[0])
dp = [0] * (max(point[0] for point in points) + 1)  # 마지막 마감일

for remainDate, point in points:
    for i in range(remainDate, 0, -1):
        dp[i] = max(dp[i], dp[i - 1] + point)
print(max(dp))
