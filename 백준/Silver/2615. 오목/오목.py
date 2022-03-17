board = [list(map(int,input().split())) for _ in range(19)]
checkBitmask = [[0 for _ in range(19)] for _ in range(19)]

dx,dy = [0,1,1,1],[1,0,1,-1]
#가로 세로 대각선

def checkIsWin(x : int, y : int,mode : int) -> int:
    #승리 여부를 반환
    color = board[x][y]
    count = 1

    posX,posY = x,y

    while True:
        checkBitmask[posX][posY] |= (1 << mode)
        posX,posY = posX + dx[mode],posY + dy[mode]

        if not(0 <= posX < 19 and 0 <= posY < 19) or \
                board[posX][posY] != color:    break    #범위 바깥이거나 색이 다른경우
        count += 1
    if count == 5:
        print(color)
        if mode != 3 : print(x + 1,y + 1)
        else: print(posX - dx[mode] + 1,posY - dy[mode] + 1)
        exit()






for i in range(19):
    for j in range(19):
        if not board[i][j]: continue    #색이 없으면 검사할 이유 X

        for mode in range(4):
            if checkBitmask[i][j] & (1 << mode): continue
            checkIsWin(i,j,mode)
print(0)