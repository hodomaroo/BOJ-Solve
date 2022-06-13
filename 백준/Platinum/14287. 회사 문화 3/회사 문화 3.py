import sys
from math import log2,ceil
#input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]

for i,boss in enumerate(list(map(int,input().split()))):
    if boss < 0: continue
    graph[boss].append(i + 1)

segmentDepth = ceil(log2(n)) + 1 #세그먼트 트리의 총 깊이
segmentTree = [0] * pow(2,segmentDepth) #세그먼트 트리의 각 노드의 값을 저장하는 배열
segmentBases = pow(2,segmentDepth - 1) #세그먼트 트리의 BaseNode의 개수(X)


nodeId = 0
preOrderCode = [0] * (n + 1) #node : preOrder
subTreeSize = [1] * (n + 1) #node : subTreeSize

def traverseTree(node : int) -> int:
    global nodeId
    preOrderCode[node] = nodeId
    nodeId += 1

    for nextnode in graph[node]:
        subTreeSize[node] += traverseTree(nextnode)

    return subTreeSize[node]

def updateNode(nodeIndex : int, value : int):
    nodeIndex = len(segmentTree) - segmentBases + nodeIndex
    segmentTree[nodeIndex] += value

    while nodeIndex:
        brotherNode = nodeIndex + (nodeIndex % 2 == 0) - nodeIndex % 2
        segmentTree[nodeIndex // 2] = segmentTree[nodeIndex] + segmentTree[brotherNode]
        nodeIndex //= 2

def getSegmentValue(left : int,right : int) -> int:
    return callSegment(1, 0, segmentBases, left, right + 1)

def callSegment(node : int, start : int, end : int, left : int, right : int) -> int:
    #구간 [start,end)를 저장하는 세그먼트 트리

    if (start, end) == (left, right):
        return segmentTree[node]
    mid = (start + end) // 2

    value = 0
    if left < mid: #[left,right)를 보므로, left < mid이면,  [start,mid)구간을 보아야 함
        value += callSegment(node * 2, start, mid, left, min(mid, right))

    if right > mid: #[left,right)이므로, right가 mid보다 커야 해당 구간을 볼 이유가 생김
        value += callSegment(node * 2 + 1, mid, end, max(left, mid), right)
    return value

traverseTree(1)
#print(subTreeSize,preOrderCode)
for i in range(m):
    query,*inform = list(map(int,input().split()))

    if query == 1:
        node, cost = inform
        updateNode(preOrderCode[node], cost)

    else:
        node = inform[0]
        if subTreeSize[node] == 1: print(0)
        else: print(getSegmentValue(preOrderCode[node], preOrderCode[node] + subTreeSize[node] - 1))

    #print(segmentTree)
