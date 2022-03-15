n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    n,c1,c2 = input().rstrip().split()
    n = ord(n) - ord("A")
    if c1.isalpha(): c1 = ord(c1) - ord("A")
    if c2.isalpha(): c2 = ord(c2) - ord("A")
    graph[n] = [c1,c2]

def preTraverse(node: int) -> None:
    print(chr(node + ord("A")),end="")
    for nextnode in graph[node]:
        if nextnode != ".": preTraverse(nextnode)

def inTraverse(node: int) -> None:
    if graph[node][0] != ".":  inTraverse(graph[node][0])
    print(chr(node + ord("A")),end="")
    if graph[node][1] != ".":  inTraverse(graph[node][1])

def postTraverse(node: int) -> None:
    if graph[node][0] != ".":  postTraverse(graph[node][0])
    if graph[node][1] != ".":  postTraverse(graph[node][1])
    print(chr(node + ord("A")), end="")

preTraverse(0)
print()
inTraverse(0)
print()
postTraverse(0)
print()
