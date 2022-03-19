from collections import defaultdict
n = int(input())
name = list(input().rstrip().split())
graph = defaultdict(list)
child = defaultdict(list)

for _ in range(int(input())):
    a,b = input().split()
    graph[a].append(b)

ancients = []
for childName in name:
    if not len(graph[childName]):
        ancients.append(childName)

    for ancient in graph[childName]:
        if len(graph[childName]) == len(graph[ancient])+1:
            child[ancient].append(childName)

print(len(ancients))
print(*sorted(ancients))
for name in sorted(graph.keys()):
    print(name,len(child[name]),*sorted(child[name]))