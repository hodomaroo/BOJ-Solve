n,m,t = map(int,input().split())
cayak = [1] * n
for i in list(map(int,input().split())):
    cayak[i-1] = 0
for i in list(map(int,input().split())):
    cayak[i-1] += 1

count = 0
for i in range(n):
    if not cayak[i]:
        count += 1

    if cayak[i] == 2:
        if i and not cayak[i-1]:
            count -= 1 #카약을 얘한테 줌

        elif i != n-1 and not cayak[i+1]:
            cayak[i + 1] = 1


print(count)

