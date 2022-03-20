import sys

input = sys.stdin.readline
from typing import List
from collections import deque
n,m,players = map(int,input().split())
conquerPerTurn = [0] + list(map(int,input().split()))
board = [list(input().rstrip()) for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]


areaPerPlayer = [0] * (players + 1)
queuePerPlayer = [deque() for _ in range(players+1)]
for i in range(n):
    for j in range(m):
        if not board[i][j].isdigit(): continue
        queuePerPlayer[int(board[i][j])].append((i,j))
        areaPerPlayer[int(board[i][j])] += 1


def bfs(playerCode: int, queue: deque) -> bool:  # update여부 리턴
    update = False
    for _ in range(conquerPerTurn[playerCode]):
        if not queue: break
        for _ in range(len(queue)):
            x,y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not(0 <= nx < n and 0 <= ny < m and board[nx][ny] == "."): continue    #정복 가능한 지역인 경우에만 확인
                queue.append((nx,ny))
                board[nx][ny] = playerCode
                areaPerPlayer[playerCode] += 1  #새로 정복한 지역만큼 칸 추가
                update = True
    return update

while True:
    update = False

    for i in range(1,players+1):    #모든 플레이어에 대해 탐색 진행
        if bfs(i,queuePerPlayer[i]):
            update = True
        #print(*board,sep="\n",end= "\n\n")

    if not update:
        print(*areaPerPlayer[1:])
        exit()

