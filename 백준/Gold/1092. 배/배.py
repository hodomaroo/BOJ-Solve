n = int(input())
crain = sorted(list(list(map(int,input().split()))))

m = int(input())
box = sorted(list(map(int,input().split())))
if crain[-1] < box[-1]:
    print(-1)
    exit()


check = [False] * m
count = m
turn = 0
while count:
    turn += 1

    last = m - 1
    for i in range(n-1,-1,-1): #자기가 가져갈 수 있는 가장 무거운걸 가져감
        for j in range(last,-1,-1):
            if not check[j] and box[j] <= crain[i]:
                check[j] = True
                count -= 1
                last = j - 1
                break
print(turn)