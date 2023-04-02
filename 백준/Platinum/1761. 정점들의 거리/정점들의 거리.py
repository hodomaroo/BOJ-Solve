import sys

RECURSION = 40001
BIT = 16

sys.setrecursionlimit(RECURSION)

n = int(input())
distance = [[[0, 0] for _ in range(BIT)] for _ in range(n + 1)]
depth = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for a, b, c in [list(map(int, input().split())) for _ in range(n-1)]:
    graph[a].append((b, c))
    graph[b].append((a, c))


def build_LCA(node: int, parent: int):
    depth[node] = depth[parent] + 1

    for i in range(1, BIT):
        ancient = distance[node][i-1]
        if distance[ancient[0]][i-1][0] == 0:
            break

        distance[node][i] = [distance[ancient[0]][i-1][0],
                             distance[ancient[0]][i-1][1] + distance[node][i-1][1]]

    for next_node, cost in graph[node]:
        if next_node == parent:
            continue

        distance[next_node][0] = [node, cost]
        build_LCA(next_node, node)


def get_distance(nodeA: int, nodeB: int) -> int:
    # make_equal
    # 항상 nodeA가 더 깊거나 동일
    if depth[nodeA] < depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA

    diff = depth[nodeA] - depth[nodeB]
    _total = 0
    for i in range(BIT):
        if (diff >> i) & 1:
            ancient = distance[nodeA][i]
            _total += ancient[1]

            nodeA = ancient[0]

    if nodeA == nodeB:
        return _total

    for i in range(BIT-1, -1, -1):
        ancientA, ancientB = distance[nodeA][i], distance[nodeB][i]

        if ancientA[0] == ancientB[0]:
            continue

        _total += ancientA[1] + ancientB[1]
        nodeA, nodeB = ancientA[0], ancientB[0]

    return _total + distance[nodeA][0][1] + distance[nodeB][0][1]


for next_node, cost in graph[1]:
    distance[next_node][0] = [1, cost]

build_LCA(1, 0)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(get_distance(a, b))
