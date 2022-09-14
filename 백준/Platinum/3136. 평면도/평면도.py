from collections import defaultdict
def solution(arrows):
    nodeDict = defaultdict(int)
    
    dx,dy = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
    #하 우 상 좌 / 좌하 우하 우상 좌상
    count = 0
    
    #대각선인 경우 교차하는 대각선이 있는지 검사
    def checkDiagonal(pos : tuple, dir : int) -> bool:
        x,y = pos
        #print(x,y,dir)
        return  (x + dx[dir], y) in nodeDict and nodeDict[(x + dx[dir], y)] & 1 << (dir + [2,6][dir % 4 == 3]) % 8
        
    x,y = 0,0
    
    for cmd in arrows:
        cmd = int(cmd)
        nx,ny = x + dx[cmd], y + dy[cmd]
            
        #새로운 간선이고, nx,ny가 이미 방문된 점인경우
        if not nodeDict[(x,y)] & 1 << cmd:
            if (nx,ny) in nodeDict:  
                count += 1

            if cmd % 2 and checkDiagonal((x,y),cmd):
                count += 1
        
        nodeDict[(x,y)] |= 1 << cmd
        nodeDict[(nx,ny)] |= 1 << (cmd + 4) % 8
        x,y = nx,ny
        
    return count

n = int(input())
cm = input()
print(solution(cm))