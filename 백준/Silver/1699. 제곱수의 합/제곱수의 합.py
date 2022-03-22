from math import sqrt

n = int(input())
#2개로 번갈아가면서 진행
dp = [[0] * (n+1) for _ in range(2)]
values = {0}

for _ in range(1,n+1):
    nextSet = values.copy()
    for v in values:
        for sqrtN in range(1,int(sqrt(n))+1):
            if v + sqrtN ** 2 not in nextSet and v + sqrtN ** 2 <= n:
                if v + sqrtN ** 2 == 100000:
                    print(v,sqrtN**2)
                nextSet.add(v + sqrtN ** 2)
    if n in nextSet:
        print(_)
        exit()
    values = nextSet
