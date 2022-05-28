import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
#불가능한 분기는 생각하지 않는다! --> -inf로 설정
dp = [[[-float("inf")] * (m + 1) for _ in range(2)] for _ in range(2)] #최대 0 ~ m번까지의 이동이 가능
inform = [0] + [int(input()) for _ in range(n)]

#1초부터 시작한다.
dp[0][0][0] = 0 #왼쪽 자두나무에서 0초에 0번 움직인 상태 == BaseCase!

for time in range(1,n + 1):
    dp[0][time % 2][0] = dp[0][1 - time % 2][0] + (inform[time] == 1)

    for move in range(1, min(m + 1, time + 1)):
        for lr in range(2):
            dp[lr][time % 2][move] = max(dp[not lr][1 - time % 2][move - 1],dp[lr][1 - time % 2][move]) + ((inform[time] - 1) == lr)
print(max(max(dp[0][n%2]),max(dp[1][n%2])))


