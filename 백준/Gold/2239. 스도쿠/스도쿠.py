#isValid로 유효성 검사하기

board = [list(map(int,list(input().rstrip()))) for i in range(9)]
valid_Row = list([True] * 9 for i in range(9))
valid_Col = list([True] * 9 for i in range(9))
valid_Grid = list([True] * 9 for i in range(9))

#해당 row에 대한 유효성 검사 / 해당 col에 대한 유효성 검사
#print(valid_Col,valid_Row)

needPos = []
for i in range(9):
    for j in range(9):
        if board[i][j]:
            valid_Row[i][board[i][j]-1] = False
            valid_Col[j][board[i][j]-1] = False
            valid_Grid[(i // 3) * 3 + (j // 3)][board[i][j] - 1] = False
        else:
            needPos.append((i,j))

#print(valid_Col,valid_Row,valid_Grid,sep="\n\n")
#print(needPos)

def dfs(posIndex : int):
    #print(posIndex)
    if posIndex == len(needPos):
        for line in board:
            print(*line,sep="")
        exit()

    i, j = needPos[posIndex]

    for v in range(9):
        if not valid_Row[i][v] or not valid_Col[j][v] or not valid_Grid[(i // 3) * 3 + (j // 3)][v]: continue
        board[i][j] = v+1
        valid_Row[i][v] = False
        valid_Col[j][v] = False
        valid_Grid[(i // 3) * 3 + (j // 3)][v] = False

        dfs(posIndex + 1)

        board[i][j] = 0
        valid_Row[i][v] = True
        valid_Col[j][v] = True
        valid_Grid[(i // 3) * 3 + (j // 3)][v] = True
dfs(0)