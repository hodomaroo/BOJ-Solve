n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(*sorted(a + b))