a,b = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        board[i][j] = max(board[i-1][j] if i else 0, board[i][j-1] if j else 0) + board[i][j]
print(board[-1][-1])
       