from typing import List

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]


def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i:
                matrix[i][j] += matrix[i - 1][j]

    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1): #구간 한정하기 [j, i]
            dict = {0 : 1}

            tot = 0
            for k in range(len(matrix[0])):
                tot = tot + matrix[i][k]

                if j:
                    tot -= matrix[j - 1][k]
                tot %= target


                if tot in dict:
                    count += dict[tot]
                    dict[tot] += 1
                else:
                    dict[tot] = 1

    return count
print(numSubmatrixSumTarget(board, k))
# 010