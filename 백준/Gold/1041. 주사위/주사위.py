from itertools import combinations,product
n = int(input())
side = list(map(int,input().split()))

#ABCDEF
#012345
graph = [[1,4,2,3],[0,5,2,3],[1,4,0,5],[1,4,0,5],[0,5,2,3],[1,4,2,3]]

if n == 1:
    print(sum(side) - max(side))
    exit()

else:
    min2Side = float("inf")
    min3Side = float("inf")

    for i in range(6):
        for comb in range(4):
            min2Side = min(min2Side, side[i] + side[graph[i][comb]])

        for comb in product([0,1],[2,3]):
            min3Side = min(min3Side, side[i] + side[graph[i][comb[0]]] + side[graph[i][comb[1]]])
    if n == 2:
        print(4 * (min2Side + min3Side))
        exit()
    else:
        print(min3Side * 4 + min2Side * (8 * n - 12) + min(side) * (pow(n - 2, 2) + 4 * (n - 1) * (n - 2)))
        exit()
