import sys
from functools import cmp_to_key

input = sys.stdin.readline

def cmp(a : int, b : int):
    return [-1, 1][str(a) + str(b) > str(b) + str(a)]

k, n = map(int,input().split())
numbers = sorted([int(input()) for _ in range(k)], key = cmp_to_key(cmp), reverse=True)
max_value = max(numbers)

for v in numbers:
    print(v if v != max_value else str(v) * (1 + n - k), end="")
    if v == max_value:
        k = n