n = int(input())
board = [[" "] * (n * 2 - 1) for _ in range(n)]

def star(starSize : int, x : int, y : int) -> list:
    if starSize == 3:
        board[x][y] = "*"
        board[x+1][y-1] = "*"
        board[x+1][y+1] = "*"

        for i in range(-2,3,1):
            board[x + 2][y + i] = "*"
        return

    star(starSize // 2, x, y)
    star(starSize // 2, x + starSize // 2, y + starSize // 2)
    star(starSize // 2, x + starSize // 2, y - starSize // 2)
star(n, 0, n - 1)
for line in board:
    print(*line, sep="")

