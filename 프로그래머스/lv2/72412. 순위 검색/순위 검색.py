from bisect import bisect_left

def solution(info, query):
    class TreeNode:
        def __init__(self): 
            self.child = {}
            self.count = 0
    
    def tree(node : TreeNode, info : int, depth : int):
        node.count += 1
        if depth == 4:  return 
        
        if info[depth] not in node.child:
            node.child[info[depth]] = TreeNode()
        tree(node.child[info[depth]], info, depth + 1)
    
    def traverse(node : TreeNode, info, depth : int):
        if depth == 4:
            return node.count
        
        if info[depth] == "-":
            return sum(traverse(childNode, info, depth + 1) for childNode in node.child.values())
        return traverse(node.child[info[depth]], info, depth + 1) if (info[depth] in node.child) else 0
    
    query = [[i] + query[i].split() for i in range(len(query))]
    info = [inform.split() for inform in info]
    
    ans = [0] * len(query)
    
    Tree = TreeNode()
    
    for inform in sorted(info + query, key = lambda x : (-int(x[-1]), len(x))):
        if len(inform) == 9:            
            ans[int(inform[0])] = traverse(Tree, inform[1::2] + [inform[0]], 0)
            
        else:
            tree(Tree, inform, 0)
    
    return ans
    