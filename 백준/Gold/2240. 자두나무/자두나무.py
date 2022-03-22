t,w = map(int,input().split())
information = [int(input()) for _ in range(t)]

dp = [[[0 for _ in range(min(31,w+1))] for _ in range(t)] for _ in range(2)]

dp[0][0][0] = [0,1][information[0] == 1]
dp[1][0][1] = [0,1][information[0] == 2]

for time in range(1,t):  #시간 순서대로 진행
    dp[0][time][0] = dp[0][time - 1][0] + [0,1][(information[time] == 1)]
    dp[1][time][0] = dp[1][time - 1][0] + [0,1][(information[time] == 2)]

    for cost in range(1,min(w,30,time)+1):
        for lr in range(2):
            #print(lr,time,cost)
            dp[lr][time][cost] = max(max(dp[lr][time-1][cost],dp[1- lr][time-1][cost-1]) + [0,1][(information[time] == lr+1)],dp[lr][time][cost-1])

#print(*dp,sep="\n")
print(max(max(dp[0][-1]),max(dp[1][-1])))

