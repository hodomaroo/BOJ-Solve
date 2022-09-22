dx,dy = [1,0,-1,0],[0,1,0,-1]

def solution(board, aloc, bloc):
    n,m = len(board),len(board[0])

    def movement(x,y,bx,by,depth):
        if not board[x][y]: #현재 위치에 발판이 없는 경우 패배
            return (0,depth)    #현재까지의 답을 리턴함

        flg = False #일단 진다로 가정
        bestMove = depth

        board[x][y] = 0

        for i in range(4):
            nx,ny = x + dx[i],y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or not board[nx][ny]: continue

            result = movement(bx,by,nx,ny,depth + 1) #(승리 여부 / 최적의 이동 턴 수)
            flg, bestMove = max((not result[0],[-1,1][result[0]] * result[1]),(flg,bestMove))

        board[x][y] = 1
        
        return (flg,abs(bestMove))

    return movement(aloc[0],aloc[1],bloc[0],bloc[1],0)[1]