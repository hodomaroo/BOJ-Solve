n,m = map(int,input().split())
birds = [input().split() for _ in range(n)]

#그냥 시간별 합을 저장해두기
timeFlow = [0] * m
ans = [float("inf"),0] #cost / index
count = 0

for i in range(m):
    for j in range(n):
        if birds[j][1][i] == "1":
            count = count - 1 if birds[j][0] == "L" else count + 1
    timeFlow[i] = count

#print(timeFlow)

for i in range(n): #각 친구가 없어질 때의 최댓값
    count = 0
    maxV = 0

    lr = -1 if birds[i][0] == "L" else 1
    for j in range(m):
        count += int(birds[i][1][j]) * lr
        #print(i,count,timeFlow[j] - count)
        maxV = max(maxV,abs(timeFlow[j] - count))

    ans = min(ans,[abs(maxV),i+1])

print(*ans[::-1],sep = "\n")





