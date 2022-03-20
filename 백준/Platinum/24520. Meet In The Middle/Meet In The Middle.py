import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

#log16까지만 필요함 2^16+a

n,tc = map(int,input().split())
graph = [[] for _ in range(n+1)]
depth = [1 for i in range(n+1)]
sparseParent = [[0 for _ in range(17)] for _ in range(n+1)] #노드번호,distance
sparseDist = [[0 for _ in range(17)] for _ in range(n+1)] #노드번호,distance
depth[0] = 0
#최대 (3log10만) * 10민
def makeTree(node,parent,cost):
    if not parent:
        depth[node] = 0
    else:
        depth[node] = depth[parent] + 1
        sparseParent[node][0] = parent
        sparseDist[node][0] = cost

        for i in range(1,17): #log로 형성하기
            sparseParent[node][i] = sparseParent[sparseParent[node][i-1]][i-1]  #희소 부모 배열
            sparseDist[node][i] = sparseDist[node][i-1] + sparseDist[sparseParent[node][i-1]][i-1]     #희소거리 배열
            if not sparseParent[node][i]: break

    for nextNode,cost in graph[node]:
        if nextNode == parent: continue
        makeTree(nextNode,node,cost)

def getLca(a,b):
    diff = depth[a] - depth[b]

    lcaDist_a = 0
    lcaDist_b = 0
    if diff:
        for i in range(17):
            if not (diff >> i) & 1: continue

            lcaDist_a += sparseDist[a][i]   #거리 증가시키기
            a = sparseParent[a][i]  #부모로 끌어올리기

            if depth[a] == depth[b]: break
    if a == b: return [a,lcaDist_a,lcaDist_b]
    #올렸을 때 동일하다면 리턴

    curA,curB = a,b
    for i in range(16,-1,-1):
        if not sparseParent[curA][i] or sparseParent[curA][i] == sparseParent[curB][i]: continue
        lcaDist_a,lcaDist_b = lcaDist_a + sparseDist[curA][i],lcaDist_b + sparseDist[curB][i]
        curA,curB = sparseParent[curA][i],sparseParent[curB][i]
    return [sparseParent[curA][0],lcaDist_a + sparseDist[curA][0],lcaDist_b + sparseDist[curB][0]]

def findEqulDist(a,b):
    if depth[a] < depth[b]: a,b = b,a

    lca,distA,distB = getLca(a,b)   #이렇게 두개 받아오기
    #print(lca, distA, distB)
    if distA == distB: return lca
    if (distA + distB) % 2 : return -1

    if distA < distB:    distB,distA,a,b = distA,distB,b,a

    cur = a
    aDist = 0

    for i in range(16,-1,-1):
        if not sparseParent[cur][i]: continue   #범위 밖인 경우 패스

        nextADist = aDist + sparseDist[cur][i]
        if nextADist > distB + (distA - nextADist): continue
        #if nextADist == distB + (distA - nextADist): return sparseParent[cur][i]

        aDist = nextADist
        cur = sparseParent[cur][i]

    return cur if aDist == distB + (distA - aDist) else -1


for _ in range(n-1):
    f,t,c = map(int,input().split())
    graph[f].append([t,c])
    graph[t].append([f,c])

makeTree(1,0,0)

for _ in range(tc):
    a,b = map(int,input().split())
    print(findEqulDist(a,b))

"""
5 1
1 2 8
2 3 10
3 4 7
5 4 3
5 2
"""