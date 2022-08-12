from bisect import bisect_left


class Node:
    def __init__(self):
        self.child = {}
        self.val = []
        self.sorted = False


def solution(info, query):
    datas = [["java", "cpp", "python"], ["backend", "frontend"],["senior","junior"], ["chicken", "pizza"]]

    index = [3, 2, 2]

    def insert(node: Node, inform: list, depth: int):
        if depth == 4:
            node.val.append(int(inform[-1]))
            #print(node.val)
            return

        if inform[depth] not in node.child:
            node.child[inform[depth]] = Node()
        insert(node.child[inform[depth]], inform, depth + 1)

    def search(node: Node, inform: list, depth):
        #print(inform, depth, node.child)
        if depth == 4:
            #print(node.val)
            #print(inform)
            return len(node.val) - bisect_left(node.val, int(inform[-1]))

        count = 0
        if inform[depth] == "-":
            for v in datas[depth]:
                if v not in node.child: continue
                count += search(node.child[v], inform, depth + 1)

        elif inform[depth] in node.child:
            count += search(node.child[inform[depth]], inform, depth + 1)

        return count

    info = sorted([inform.split() for inform in info], key=lambda x: int(x[-1]))
    root = Node()
    for inform in info:
        insert(root, inform, 0)

    answer = []
    for q in query:
        answer.append(search(root, q.split()[0::2] + [q.split()[-1]], 0))

    return answer
