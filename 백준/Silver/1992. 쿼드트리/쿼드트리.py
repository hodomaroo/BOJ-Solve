from typing import List
#그냥 영역 사분할해서 재귀로 넣기
#영역 크기가 1 * 1이 되면 리턴 (자기 값)
#4개 값이 다 같으면 해당 값 리턴하기
#그렇지 않으면 괄호씌우기
n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]

def QuadTree(x : int ,y : int, sizeLen : int) -> str:
    if sizeLen == 1:
        return grid[x][y]

    else:
        v1 = QuadTree(x, y, sizeLen // 2)
        v2 = QuadTree(x, y + sizeLen // 2, sizeLen // 2)
        v3 = QuadTree(x + sizeLen // 2, y, sizeLen // 2)
        v4 = QuadTree(x + sizeLen // 2, y + sizeLen // 2, sizeLen // 2)

        if v1 == v2 == v3 == v4 and v1 in ("1","0"):
            return v1
        else:
            return "(" + v1 + v2 + v3 + v4 +")"
print(QuadTree(0,0,n))
