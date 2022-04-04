from collections import deque

capas = list(map(int,input().split()))
resultSet = set()
statusSet = set()

queue = deque([[0,0,capas[2]]])

direct = [(0,1),(0,2),(1,2),(1,0),(2,0),(2,1)]


while queue:
    amounts = queue.popleft()
    #총 6가지 방법이 존재

    for f,t in direct:
        if not amounts[f] or amounts[t] == capas[t]: continue

        nextAmounts = list(amounts[:])
        remain = amounts[f] + amounts[t] - capas[t]
        if remain <= 0 :
            remain = 0
            nextAmounts[f] = 0
            nextAmounts[t] = amounts[f] + amounts[t] #다 못채운 경우

        else:
            nextAmounts[f] = remain
            nextAmounts[t] = capas[t] #다 채우고도 남은 경우

        nextAmounts = tuple(nextAmounts)

        if nextAmounts in statusSet: continue

        statusSet.add(nextAmounts)

        if not nextAmounts[0]:
            resultSet.add(nextAmounts[2])
        queue.append(nextAmounts)

print(*sorted(resultSet))