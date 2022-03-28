n,m,c = map(int,input().split())
dx,dy = [0,1,0,-1],[1,0,-1,0]
board = [list(map(int,input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

regions = []

for i in range(min(n,m)//2):  #더 작은거 //2 회 만큼의 로테이션이면 충분함
    x,y = i,i
    region = [(x, y)]
    check[x][y] = True

    for dir in range(4):
        while True:
            nx,ny = x + dx[dir],y + dy[dir]
            if not (0 <= nx < n and 0 <= ny < m) or check[nx][ny]: break
            check[nx][ny] = True
            region.append((nx,ny))
            x, y = nx, ny

    regions.append(region)
for idx,region in enumerate(regions):
    saveValue = board[region[0][0]][region[0][1]]
    nextvalue = [0] * len(region)

    for i in range(len(region)):
        tx,ty = region[(i + c)%len(region)]
        nextvalue[i] = board[tx][ty]

    for i in range(len(region)):
        x,y = region[i]
        board[x][y] = nextvalue[i]
for line in board:
    print(*line)