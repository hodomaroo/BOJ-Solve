n,m = map(int,input().split())
board = [input().replace(".", "D") for _ in range(n)]
dx,dy = [1,0,-1,0], [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if board[i][j] == "W":
            for k in range(4):
                x,y = i + dx[k], j + dy[k]
                if 0 <= x < n and 0 <= y < m and board[x][y] == "S":
                    print(0)
                    exit(0)

print(1)
print(*board, sep = "\n")
            

