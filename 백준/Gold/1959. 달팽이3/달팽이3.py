n,m = map(int,input().split())

def lastJudge(n : int, m : int) -> tuple:
    # 크기가 n,m인 직사각형 기준으로
    #현재 xy위치가 끝임

    if m * n == 1: #둘다 1인 경우 계산대로 나옴
        return (0,0,0) #그냥 자기 위치

    elif m == 1:
        return (1, n - 1, 0)  # 아래쪽으로 한번 더 꺾을 수 있음 n만큼

    elif n == 1:
        return (0, 0, m - 1)  # 꺾임은 그대로

    elif n == 2:    #위치는 무조건 2,1
        return (2,1,0)  # 무조건 두번꺾임 (우선순위 높음)

    elif m == 2:
        return (3,1,0)  # 무조건 세번꺾임

rotate = ((min(n,m) + min(n,m)%2) // 2 - 1)
x,y = 1 + rotate,1 + rotate

n -= rotate * 2
m -= rotate * 2
#print(n,m)
edge,jx,jy = lastJudge(n,m)
print(4 * rotate + edge)
print(x + jx, y + jy)
