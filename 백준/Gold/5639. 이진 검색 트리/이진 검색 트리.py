import  sys
sys.setrecursionlimit(10**5)

nodes = []
try:
    while True:
        nodes.append(int(input()))
except: pass
nodes.reverse()

def dfs(parent):
    node = nodes.pop()
    if nodes and nodes[-1] < node:
        dfs(node)
    if nodes and nodes[-1] > node and nodes[-1] < parent :
        dfs(parent)
    print(node)
dfs(float("inf"))
