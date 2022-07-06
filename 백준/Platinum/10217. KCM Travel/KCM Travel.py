from math import inf
import heapq

def dijkstra(start):
    heap = []
    #시간 / 돈
    check = [[inf for _ in range(M+1)] for _ in range(N+1)]

    check[1][0] = 0

    heapq.heappush(heap,(0,0,start))    #(시간/돈/노드)

    while heap:
        nowTime,nowCost,nowNode = heapq.heappop(heap)

        if nowNode == N:
            return nowTime

        for nextNode,cost,time in graph[nowNode]:
            nextTime = time + nowTime
            nextCost = cost + nowCost

            if nextCost > M: continue

            if nextTime < check[nextNode][nextCost]:
                for costArea in range(nextCost,M+1):
                    if check[nextNode][costArea] > nextTime:
                        check[nextNode][costArea] = nextTime
                    else:
                        break
                heapq.heappush(heap,(nextTime,nextCost,nextNode))
    return "Poor KCM"

testcase = int(input())
res = []
for _ in range(testcase):

    N,M,K = list(map(int,input().split()))

    graph = [[] for _ in range(N+1)]

    for __ in range(K):
        a,b,s,d = list(map(int,input().split()))
        graph[a].append([b,s,d])  #티켓 정보 추가

    res.extend([dijkstra(1)])

print(*res,sep="\n")

