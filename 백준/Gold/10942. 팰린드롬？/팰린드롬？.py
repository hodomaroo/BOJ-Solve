#펠린드롬?
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
isPel = [[0] * n for _ in range(n)]
#N * N 격자크기
for i in range(n):
    isPel[i][i] = True #자기 자신은 무조건 펠린드롬
    if i < n-1: isPel[i][i+1] = (numbers[i] == numbers[i+1])

for diff in range(2,n):
    for i in range(n - diff):
        isPel[i][i + diff] = isPel[i+1][i + diff-1] & (numbers[i] == numbers[i + diff])

#쿼리 수행
for _ in range(int(input())):
    s,e = map(int,input().split())
    print(int(isPel[s-1][e-1]))
