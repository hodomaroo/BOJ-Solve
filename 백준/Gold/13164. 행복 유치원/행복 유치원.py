n,m = map(int,input().split())
peo = list(map(int,input().split()))
peo = sorted([peo[i] - peo[i-1] for i in range(1,n)], reverse= True)
print(sum(peo[m-1:]))

