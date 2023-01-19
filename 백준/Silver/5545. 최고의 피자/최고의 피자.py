from itertools import accumulate

n = int(input())
a,b = map(int, input().split())
dough = int(input())
tops = list(accumulate(sorted([int(input()) for _ in range(n)], reverse= True)))

print(max(dough // a, max((dough + tops[i]) // ( a + b * (i + 1)) for i in range(n))))