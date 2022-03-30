import sys

input = sys.stdin.readline
n,m = map(int,input().split())
numbers = list(map(int,input().split()))
prefix = [0 for i in range(n)]
for i in range(n):
    prefix[i] = prefix[i-1] + numbers[i]

#print(*prefix)
for _ in range(m):
    f,t = map(int,input().split())
    print(prefix[t-1] - (0 if f-2 < 0 else prefix[f-2]))


