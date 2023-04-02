n, m = map(int, input().split())
nums = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for a, b in [list(map(int, input().split())) for _ in range(n-1)]:
    graph[a].append(b)
    graph[b].append(a)


def treeDP(node: int, parent: int) -> list[int]:
    # [노드에 설치한 우물 수, 필요한 우물, 현재까지 설치한 총 우물 수]
    if len(graph[node]) == 1 and parent != -1:
        return [0, nums[node - 1], 0]

    next_well, need_well, total_well = 0, 0, 0
    for next_node in graph[node]:
        if parent != next_node:
            a, b, c = treeDP(next_node, node)
            next_well += a
            need_well = max(need_well, b)
            total_well += c
            
    return [need_well, max(0, nums[node - 1] - need_well - next_well), total_well + need_well]


print(sum(treeDP(1, -1)[1:]))
