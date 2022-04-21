from collections import deque
import sys,os

def BFS(p,amount):
    queue = deque()
    dx,dy = [1,-1,0,0],[0,0,1,-1]

    visit[p[0]][p[1]] = 1
    queue.append(p)

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ny,nx = y + dy[i],x + dx[i]

            if 0 <= nx < N and 0 <= ny < N and region[ny][nx] > amount and not visit[ny][nx]:
            #다음 점이 범위 안이며 높이가 물의 양보다 더 많으며, 방문한 점이 아닐 경우
                queue.append([ny,nx])
                visit[ny][nx] = 1


N = int(sys.stdin.readline())

region,highest = list(),1
max_safezone = 1 # 하나도 잠기지 않은 경우


for i in range(N):
    region_line = list(map(int,sys.stdin.readline().split()))
    highest = max(highest,max(region_line)) # 현재의 highest값과 region 높이를 비교 / 최대값 갱신
    #lowest = min(highest, min(region_line))  # 현재의 lowest값과 region 높이를 비교 / 최솟값 갱신
    region.append(region_line)

#print(region)

for rain_amount in range(1,highest):
    safezone = 0
    visit = [[0] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if region[y][x] > rain_amount and not visit[y][x]:
                #방문한 적 없고 고도가 더 높은 경우에만 탐색의 가치가 있음
                safezone += 1
                BFS([y,x],rain_amount)

    #print(safezone,rain_amount,*visit,sep='\n',end='\n\n')
    max_safezone = max(max_safezone,safezone)

print(max_safezone)


