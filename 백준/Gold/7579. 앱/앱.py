n,m = map(int,input().split())
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))

dp = [-float("inf")] * 10001 #최대 10001까지 가능
dp[0] = 0
#dp[x] = cost가 x일 때 만들수 있는 최대 메모리

for index in range(len(costs)):
    for cost in range(10000, costs[index] - 1, -1):
        dp[cost] = max(dp[cost],dp[cost - costs[index]] + memories[index])

for i in range(10001):
    if dp[i] >= m:
        print(i)
        exit()

