from collections import Counter
n = int(input())
a,b = Counter(list(map(int, input().split()))),Counter(list(map(int, input().split())))
print(n - sum((a & b).values()))