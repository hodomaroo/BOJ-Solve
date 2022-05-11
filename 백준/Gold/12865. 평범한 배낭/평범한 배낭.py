n,w = map(int,input().split())
obj = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (w + 1) #--> 0개의 물건이 있으면 최대 가치
#--> dp[x] --> x무게의 물건을 담았을 때의 최대 가치

for weight,value in obj:
    for i in range(w - weight, -1, -1):  # w - weight + w -> w dp[w]
        dp[i + weight] = max(dp[i + weight], dp[i] + value)
#print(dp)
print(max(dp))



