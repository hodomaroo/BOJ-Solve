from bisect import bisect_right

class Node:
    def __init__(self):
        self.child = {}
        self.val = []

def solution(info, query):
    datas = [["java","cpp","python"],["backend","frontend"],["chicken","pizza"]]
    
    index = [3,2,2]
    
    def insert(node : Node, inform : list, depth : int):
        if depth == 3:
            node.val.append(inform[-1])
            print(node.val)
            return 
        
        if inform[depth] not in node.child:
            node.child[inform[depth]] = Node()
        insert(node.child[inform[depth]], inform, depth + 1)
    
    def search(node : Node, inform : list, depth):
        if depth == 3:
            return bisect_right(node.val, inform[-1])
        
        count = 0
        if inform[depth] == "-":
            for v in datas[depth]:
                if v not in node.child: continue
                count += search(node.child[v], inform, depth + 1)
        
        return count
    
    root = Node()
    for inform in info:
        insert(root, inform, 0)
    
    answer = []
    for q in query:
        answer.append(search(root, q.split()[0::2],0))
    
    return answer