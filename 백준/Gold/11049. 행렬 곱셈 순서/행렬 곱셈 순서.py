values = [list(map(int,input().split())) for _ in range(int(input()))]
if len(values) == 1:
    print(0)
    exit()

dp = [[0] * len(values) for _ in range(len(values))]

for i in range(len(values)-1):
    dp[i][i + 1] = values[i][0] * values[i + 1][0] * values[i + 1][1]

for diff in range(2,len(values)):
    for i in range(len(values)):
        if i + diff >= len(values): break

        dp[i][i + diff] = float("inf")
        for div in range(i,i + diff):
            #print(div)
            dp[i][i + diff] = min(dp[i][i + diff],dp[i][div] + dp[div + 1][i + diff] + values[i][0] * values[i + diff][1] * values[div][1])

print(dp[0][-1])