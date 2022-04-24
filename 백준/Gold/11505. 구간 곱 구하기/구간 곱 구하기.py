import sys
from math import log2,ceil
input = sys.stdin.readline

n,m,k = map(int,input().split())
MOD = 1000000007

segmentDepth = ceil(log2(n)) + 1
segmentTree = [1] * pow(2,segmentDepth)
segmentBases = pow(2,segmentDepth - 1)

def updateNode(nodeIndex : int, value : int):
    nodeIndex = len(segmentTree) - segmentBases + nodeIndex
    originalValue = segmentTree[nodeIndex]
    segmentTree[nodeIndex] = value

    while nodeIndex:
        brotherNode = nodeIndex + (nodeIndex % 2 == 0) - nodeIndex % 2
        segmentTree[nodeIndex // 2] = (segmentTree[nodeIndex] * segmentTree[brotherNode]) % MOD
        nodeIndex //= 2

def getSegmentValue(left : int,right : int) -> int:
    return callSegment(1, 0, segmentBases, left, right + 1)

def callSegment(node : int, start : int, end : int, left : int, right : int) -> int:
    #구간 [start,end)를 저장하는 세그먼트 트리
    #print(start,end,left,right)
    if (start, end) == (left, right):
        return segmentTree[node]
    mid = (start + end) // 2

    value = 1

    if left < mid: #왼쪽 영역을 먹어야 함
        value *= callSegment(node * 2, start, mid, left, min(mid, right))

    if right > mid: #같아도 mid를 포함해야함

        #right는 반드시 원하는 영역의 끝
        #but left도 mid + 1보다 클 수 있으므로 연산

        value *= callSegment(node * 2 + 1, mid, end, max(left, mid), right)
    return value % MOD


for i in range(n):
    updateNode(i,int(input()))

for i in range(m + k):
    mode,a,b = map(int,input().split())
    if mode == 1:
        updateNode(a - 1,b)
        #print(segmentTree)
    else:
        print(getSegmentValue(a - 1, b - 1))