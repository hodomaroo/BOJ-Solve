n = int(input())
k = int(input())    #k개의 색 선택
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
#색을 k개 선택하는 경우의 수
dp[0] = [1] * (n + 1)
dp[1][1] = 1
#dp[k][n] --> n개의 색 중 k개를 선택하는 경우의 수

for i in range(2,n+1):    #색이 중요(중복 허용 X)
    for j in range(1,k+1):
        if j * 2 > i + 1: break
        dp[j][i] = (dp[j-1][i-2] + dp[j][i-1])%1000000003
        #이전꺼 칠하고 이거 안칠하기
        #이거 칠하고 이전꺼 안칠하기
print((dp[k-1][n-3] + dp[k][n-1])%1000000003)


