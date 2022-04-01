import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    chapters = list(map(int,input().split()))
    chapterPrefix = [0] * n
    for i in range(n):
        chapterPrefix[i] = chapterPrefix[i-1] + chapters[i]

    dp = [[float("inf")] * n for _ in range(n)] #챕터 x ~ y까지 연결하는데 최소

    for i in range(0,n):
        dp[i][i] = 0
        if i: dp[i - 1][i] = chapters[i] + chapters[i - 1]  # 두개짜리 합치는데 비용 #한개를 합치는데 비용은..? 그냥 하나로 치면 되지 않을까


    for turm in range(2,n):    #
        for i in range(n-turm): #n - turm까지만 확인 가능
            for div in range(turm): #
                #print(turm,i,div,i + div + 1)
                dp[i][i + turm] = min(dp[i][i + turm],dp[i][i + div] + dp[i + div + 1][i + turm] + chapterPrefix[i + turm] - (0 if i == 0 else chapterPrefix[i - 1]))  # 누적으로 값이 들어감 #이전 합 + 이번에 만들어지는 파일 크기

    #print(*dp, sep="\n")
    print(dp[0][-1])




