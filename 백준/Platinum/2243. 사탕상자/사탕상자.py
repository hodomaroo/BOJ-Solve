import sys
from math import ceil, log2
input = sys.stdin.readline

segDepth = ceil(log2(1000000)) #총 시작노드는 100만개
segmentTree = [0] * pow(2,segDepth + 1)
segBaseNodes = pow(2, segDepth) #ba
#segment index starts from 1


#node : segbaseNode -> starts from 0
def updateSegment(node : int, v : int):
    #print(node,len(segmentTree),segBaseNodes)
    node = len(segmentTree) - segBaseNodes + node
    segmentTree[node] += v # -> add v to node

    while node:
        node //= 2
        segmentTree[node] += v #simply just add v to all parent nodes

#return index of Nth delicious candy
def traverseSegment(node : int, nth : int) -> int:
    #print(node,nth)
    if node * 2 >= len(segmentTree):
        return node - len(segmentTree) + segBaseNodes #-> return index of right base node

    if nth > segmentTree[node * 2]:
        return traverseSegment(node * 2 + 1, nth - segmentTree[node * 2])
    else:
        return traverseSegment(node * 2, nth)

for _ in range(int(input())):
    query = list(map(int,input().rstrip().split()))
    if query[0] == 1:
        node = traverseSegment(1, query[1])
        updateSegment(node, -1)
        print(node)

    else:
        updateSegment(query[1], query[2])
