n,m = map(int,input().split())
#불가능한 분기는 생각하지 않는다! --> -inf로 설정
dp = [[[-float("inf")] * (m + 1) for _ in range(n + 1)] for _ in range(2)] #최대 0 ~ m번까지의 이동이 가능
inform = [0] + [int(input()) for _ in range(n)]

#1초부터 시작한다.
dp[0][0][0] = 0 #왼쪽 자두나무에서 0초에 0번 움직인 상태 == BaseCase!

for time in range(1,n + 1):
    dp[0][time][0] = dp[0][time - 1][0] + (inform[time] == 1)
    for move in range(1, min(m + 1, time + 1)):
        for lr in range(2):
            dp[lr][time][move] = max(dp[not lr][time - 1][move - 1],dp[lr][time - 1][move]) + ((inform[time] - 1) == lr)

#print(*dp,sep="\n")
print(max(max(dp[0][-1]),max(dp[1][-1])))


