from functools import cmp_to_key

def cmp(a : str, b : str):
    return [-1, 1][a + b > b + a]


k, n = map(int,input().split())
numbers = sorted([input() for _ in range(k)], key = cmp_to_key(cmp), reverse=True)

max_value = 0
for v in numbers:
    max_value = max(max_value, int(v))

for v in numbers:
    print(v if v != str(max_value) else v * (1 + n - k), end="")
    if v == str(max_value):
        k = n
