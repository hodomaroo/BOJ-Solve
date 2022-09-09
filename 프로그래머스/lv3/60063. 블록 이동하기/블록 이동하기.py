from collections import deque
from typing import List
def solution(board : List[List[int]]):
    n = len(board)
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    
    def getMainPoint(x : int, y : int, d : int) -> List[int]: #x,y,d
        if d >= 2: #0 or 3(위 or 왼쪽을 바라보는 경우) 
            x,y,d = x + dx[d],y + dy[d],(d + 2) % 4
        return x,y,d
    
    def validPoint(x : int, y : int) -> bool:
        return 0 <= x < n and 0 <= y < n and not board[x][y]
    
    #0 1 2 3 위 오른쪽 아래 왼쪽
    dp[0][0][0] = 1
    queue = deque([(0,0,0)])
    
    while queue:
        x,y,d = getMainPoint(*queue.popleft()) #포인트는 무조건 왼쪽 / 위쪽 포인트로 기술
        xx,yy = x + dx[d], y + dy[d]
        
        if (xx,yy) == (n-1, n-1):
            break
            
        for i in range(4):
            nx,ny,nxx,nyy = x + dx[i], y + dy[i], xx + dx[i], yy + dy[i]
            if validPoint(nx,ny) and validPoint(nxx,nyy): #mainPoint에 대해서만 검사\
                if not dp[nx][ny][d]:
                    queue.append((nx,ny,d))
                    dp[nx][ny][d] = dp[x][y][d] + 1
                
                if d ^ i: #위상이 90도 차이인 경우
                    for rx,ry,rd in [getMainPoint(x,y,i), getMainPoint(xx,yy,i)]:
                        if not dp[rx][ry][rd]:
                            queue.append((rx,ry,rd))
                            dp[rx][ry][rd] = dp[x][y][d] + 1
    print(dp)
    return dp[x][y][d] - 1