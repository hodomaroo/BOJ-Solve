import sys
input = sys.stdin.readline
count = 0
from itertools import combinations
#18C9 -> 48620 에 대해서, 그리디하게 파라매트릭 서치 구현하기
#-> 특정 영역이 선택한 값을 넘으면 라인 하나 추가하기!
# 시간복잡도 O(18C9 * log2(all Sum)(Binary) * (n or m (linear Greedy)
# 48620 * 30(log2(2 * 10^6 * 18^2) * 18 -> 13,127,400 * 18
# O(Combination(24310 -> 17C9) * Binary Search(30) * 9 ^ 2

def Check(limit : int, case : list):
    prevCol, cnt = 0,0
    col = 0

    while col < m:
        prevRow = 0
        flg = 1

        for row in comb:
            areaSum = prefixArr[row][col]

            if prevRow: areaSum -= prefixArr[prevRow - 1][col]
            if prevCol: areaSum -= prefixArr[row][prevCol - 1]
            if prevRow and prevCol: areaSum += prefixArr[prevRow - 1][prevCol - 1]

            if col == prevCol and areaSum > limit:
                return False #-> 불가능한 경우 / 영역 한줄이 더 큼

            if areaSum > limit:
                cnt, prevCol = cnt + 1, col
                flg = 0
                break

            prevRow = row + 1

        col += flg
    #print(case, limit, cnt)
    return cnt <= q #사용한 라인 수가 q개 이하

def RCheck(limit : int, case : list):
    prevCol, cnt = 0,0
    col = 0

    while col < m:
        prevRow = 0
        flg = 1

        for row in range(len(comb)-1, -1, -1):
            row = comb[row]
            areaSum = prefixArr[row][col]

            if prevRow: areaSum -= prefixArr[prevRow - 1][col]
            if prevCol: areaSum -= prefixArr[row][prevCol - 1]
            if prevRow and prevCol: areaSum += prefixArr[prevRow - 1][prevCol - 1]

            if col == prevCol and areaSum > limit:
                return False #-> 불가능한 경우 / 영역 한줄이 더 큼

            if areaSum > limit:
                cnt, prevCol = cnt + 1, col
                flg = 0
                break

            prevRow = row + 1

        col += flg
    #print(case, limit, cnt)
    return cnt <= q #사용한 라인 수가 q개 이하

n, m, r, q = map(int, input().split())
prefixArr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i > 0:   prefixArr[i][j] += prefixArr[i - 1][j]
        if j > 0:   prefixArr[i][j] += prefixArr[i][j - 1]
        if i > 0 and j > 0:   prefixArr[i][j] -= prefixArr[i - 1][j - 1]


#stat : bit(select) row / lines : comb gen. line / rem : remain select chance

ans = prefixArr[-1][-1]

for comb in list(combinations(range(n - 1), r)):
    comb = list(comb) + [n - 1]

    l, r = 0, prefixArr[-1][-1] + 2  # 배열 최대 크기

    while l + 1 < r:
        mid = (l + r) // 2

        if Check(mid, comb) or RCheck(mid, comb):
            r = mid
        else:
            l = mid

    ans = min(ans, r)

print(ans)

"""
18 18 9 9
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
"""