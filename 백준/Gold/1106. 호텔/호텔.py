c,n = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]

dp = [float("inf") for _ in range(c + 100)]
#--> 손님을 X명 늘이기 위해 필요한 최소 비용
dp[0] = 0

for cost,customer in table:
    for i in range(len(dp) - customer): #최대 디피 영역까지 구하기
        dp[i + customer] = min(dp[i + customer], dp[i] + cost) #실제로 가능한 값

print(min(dp[c:]))
