from collections import  deque
from copy import deepcopy


n = int(input())
board = []
history = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
max_block = 0
def moveBlock(m,idx):
    global max_block
    board = deepcopy(m)

    isChange = 0
    if idx == 0:

        for x in range(n):

            stack = 0
            for y in range(1,n):
                if board[y][x]:
                    temp = board[y][x]
                    board[y][x] = 0

                    if board[stack][x] == temp:
                        board[stack][x] = temp * 2
                        max_block = max(temp * 2, max_block)
                        stack += 1

                        isChange = 1

                    elif board[stack][x] == 0:
                        board[stack][x] = temp

                    else:
                        stack += 1
                        board[stack][x] = temp
                        isChange =  isChange or (stack != y)
    elif idx == 1:

        for y in range(n):
            stack = 0
            for x in range(1, n):
                if board[y][x]:
                    temp = board[y][x]
                    board[y][x] = 0

                    if board[y][stack] == temp:
                        board[y][stack] = temp * 2
                        max_block = max(temp * 2, max_block)
                        stack += 1
                        isChange = 1

                    elif board[y][stack] == 0:
                        board[y][stack] = temp


                    else:
                        stack += 1
                        board[y][stack] = temp
                        isChange =  isChange or (stack != x)

    elif idx == 2:

        for x in range(n):
            stack = n-1
            for y in range(n-2,-1,-1):
                if board[y][x]:
                    temp = board[y][x]
                    board[y][x] = 0

                    if board[stack][x] == temp:
                        board[stack][x] = temp * 2
                        max_block = max(temp * 2, max_block)
                        stack -= 1
                        isChange = 1

                    elif board[stack][x] == 0:
                        board[stack][x] = temp


                    else:
                        stack -= 1
                        board[stack][x] = temp
                        isChange =  isChange or (stack != y)

    elif idx == 3:

        for y in range(n):
            stack = n-1
            for x in range(n-2,-1,-1):
                if board[y][x]:
                    temp = board[y][x]
                    board[y][x] = 0

                    if board[y][stack] == temp:

                        board[y][stack] = temp * 2
                        max_block = max(temp * 2,max_block)
                        stack -= 1
                        isChange = 1

                    elif board[y][stack] == 0:
                        board[y][stack] = temp

                    else:
                        stack -= 1
                        board[y][stack] = temp
                        isChange =  isChange or (stack != x)
    return (board,isChange)

def BFS():

    while queue:
        dp,board = queue.popleft()


        if dp > 5:
            break

        for i in range(4): #4방향
            nextBoard,changed = moveBlock(board,i)

            if not changed:
                continue

            queue.append((dp+1,nextBoard))

#보드 입력받기
max_block = 0
for i in range(n):
    line = list(map(int,input().split()))
    board.append(line)

    for num in line:
        max_block = max(max_block,num)



queue = deque([(1,board)])
BFS()
print(max_block)