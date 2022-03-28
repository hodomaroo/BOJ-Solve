n = int(input())
m = int(input())
dx,dy = [1,0,-1,0],[0,1,0,-1]

x,y = 0,0
count = 0
tx,ty = 0,0

board = [[0] * n for _ in range(n)]
board[x][y] = n * n

while True:
    nx, ny = x + dx[count % 4], y + dy[count % 4]
    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny]:
        count += 1
        nx, ny = x + dx[count % 4], y + dy[count % 4]

    if board[nx][ny]:
        for v in board:
            print(*v)
        print(tx + 1, ty + 1)
        exit()

    board[nx][ny] = board[x][y] - 1
    x,y = nx,ny

    if board[x][y] == m:    tx,ty = x,y