import sys
from math import log2,ceil
input = sys.stdin.readline


#union-find functions -------------------

def getParent(node : int) -> int:
    while parent[node] != node:
        node = parent[node]
    return node

def isUnion(nodeA : int, nodeB : int) -> bool:
    return getParent(nodeA) == getParent(nodeB)
    
def union(nodeA : int, nodeB : int) -> bool:
    if isUnion(nodeA,nodeB):
        return False
    
    pa,pb = getParent(nodeA),getParent(nodeB)
    if rank[pa] < rank[pb]:
        parent[pa] = pb
    else:
        parent[pb] = pa
        rank[pa] += (rank[pa] == rank[pb])
    return True
#-------------------------------------------

#Push Link into segmentNode
def pushLink(node : int, low : int, high : int, left : int, right : int, information : list[int]) -> None:
    if left <= low and high <= right: #현재 구간 안에 있는 경우
        querySegment[node].append(information)
        return
    
    mid = (low + high) // 2
    if left <= mid:
        pushLink(node * 2, low, mid, left, right, information)
    if right >= mid + 1:
        pushLink(node * 2 + 1, mid + 1, high, left, right, information)

#---------------------------

#Query Processing Function 
#현재 노드의 특정 간선에 의해서 새로 연결되는 트리끼리 병합
#해당 간선을 스택에 저장
#현재 노드가 base노드인 경우 -> 쿼리 처리
#스택에 있는 간선들은 수명이 끝난 간선이므로 RollBack 처리
def QueryTraverse(node : int, low : int, high : int) -> None:
    usedLinkStack = []
    
    for nodeA,nodeB in querySegment[node]: #현재 노드에 있는 쿼리들 검사하기
        pa,pb = getParent(nodeA),getParent(nodeB)
        rankup = (rank[pa] == rank[pb])
        if union(nodeA,nodeB):
            #print("CONNECT", nodeA, nodeB)
            usedLinkStack.append((nodeA,nodeB,pa,pb, rankup)) #연결된 경우만 넣어주기
    
    if low == high: #0부터 쭈욱...
        if len(result) < len(queryStack):
            result.append(int(isUnion(*queryStack[low])))
    else:
        mid = (low + high) // 2
        QueryTraverse(node * 2, low, mid)
        QueryTraverse(node * 2 + 1, mid + 1, high)
    
    while usedLinkStack:
        nodeA,nodeB,lastRootA, lastRootB, rankup = usedLinkStack.pop() #현재 노드에 있는 쿼리들 검사하기    
        #connection Rollback (rank, root)
        #print("ROLLBACK", nodeA, nodeB)
        
        parent[lastRootA],parent[lastRootB] = lastRootA,lastRootB
        rank[lastRootA] -= rankup 
    return   
#---------------------------

nodes, queries = map(int,input().rstrip().split())
graphStack = []

graphs = [dict() for _ in range(nodes + 1)]

linkHistory = [] #현재까지 들어온 간선들 리스트  -> 마지막까지 끊어지지 않는 간선 처리
graphStack = [] #삽입할 간선 리스트
queryStack = [] #처리해야 할 3번 쿼리 리스트
result = [] #쿼리 결과

#간선 수명따라 linkHistory에 로그 기록 / graphStack에 수명 구간 등록(끊어지는 경우)
for _ in range(queries):
    t,a,b = map(int,input().rstrip().split())
    
    if a > b:
        a,b = b,a   
        
    if t == 1:
        graphs[a][b] = len(queryStack)
        linkHistory.append((a,b))
    
    elif t == 2:
        if len(queryStack) != graphs[a][b]:
            graphStack.append([a,b,graphs[a][b],len(queryStack) - 1]) #구간 [a,b] 
        graphs[a].pop(b)
    else:
        queryStack.append((a,b))
    
for a,b in linkHistory:
    if b in graphs[a]:
        graphStack.append([a,b,graphs[a][b],len(queryStack)])
        graphs[a].pop(b)
        
        

parent = [i for i in range(nodes + 1)]
rank = [0 for i in range(nodes + 1)]
querySegDepth = ceil(log2(len(queryStack))) #세그먼트 트리 깊이
querySegment = [[] for _ in range(pow(2, querySegDepth + 1))] #세그먼트 트리 노드 개수

for nodeA, nodeB, start, end in graphStack:
    pushLink(1,0,pow(2,querySegDepth) - 1,start,end,[nodeA,nodeB]) #전체 링크 삽입

#쿼리 종합 처리
QueryTraverse(1,0,pow(2,querySegDepth) - 1)

#결과 출력
if len(result):
    print(*result, sep = "\n")