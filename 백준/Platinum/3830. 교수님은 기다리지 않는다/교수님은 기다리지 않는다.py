import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def findParent(a):
    #print(a,parent[a])
    if parent[a] == a: return a

    par = findParent(parent[a])
    relativeWeight[a] += relativeWeight[parent[a]]
    parent[a] = par
    return par

def union(a,b,val):
    #b가 a보다 val만큼 무겁다
    #--> a는 b보다 val만큼 가볍다
    rootA,rootB = findParent(a),findParent(b)

    if rootA == rootB: return

    parent[rootB] = rootA
    relativeWeight[rootB] = relativeWeight[a] - relativeWeight[b] + val

def isUnion(a,b):
    return findParent(a) == findParent(b)

def getWeight(a):
    #자기가 부모가 아니면 상대 무게 가짐
    if parent[a] != a:  return relativeWeight[a] + getWeight(parent[a])
    return 0 #부모라면 0 리턴

while True:
    n,m = map(int,input().rstrip().split())
    parent = [i for i in range(n+1)]
    rank = [0] * (n + 1)
    relativeWeight = [0] * (n + 1)

    if not n and not m: exit(0)

    for _ in range(m):
        func = list(input().rstrip().split())

        if func[0] == "!":  #disjoint 정의
            #print("DIS")
            a,b,v = map(int,func[1:])
            union(a,b,v)
            #print(relativeWeight)
        elif func[0] == "?": #쿼리
            a, b = map(int, func[1:])
            if isUnion(a,b):
                print(relativeWeight[b] - relativeWeight[a])
            else: print("UNKNOWN")
    #print(list(getWeight(i) for i in range(1,n+1)))