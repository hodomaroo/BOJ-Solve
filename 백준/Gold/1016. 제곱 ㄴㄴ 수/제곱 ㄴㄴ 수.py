from math import sqrt,ceil

n,m = map(int,input().split())
length = min(1000001,int(sqrt(m)) + 1)

isPrime = [True] * length
isPrime[0] = isPrime[1] = False
primes = []

for i in range(2,length):
    if not isPrime[i]: continue
    primes.append(i)

    for j in range(i * 2, length, i):
        isPrime[j] = False

powNoNo = [True] * (m - n + 1)
count = len(powNoNo)

for v in primes:
    power = v ** 2
    start = ceil(n / power) * power - n
    for i in range(start, len(powNoNo), power):
        count -= powNoNo[i]

        if powNoNo[i]:
            powNoNo[i] = False

print(count)
#power가 위치해야 하는 인덱스
