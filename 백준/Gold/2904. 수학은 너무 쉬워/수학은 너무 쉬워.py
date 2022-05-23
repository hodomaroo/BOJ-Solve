from typing import List
from math import sqrt

def getPrimes(limit : int) -> List[bool]:
    isPrime = [True] * (limit + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2,int(sqrt(limit)) + 1):
        if not isPrime[i]: continue

        for n in range(i * i, limit + 1, i):
            isPrime[n] = False
    return [i for i in range(limit + 1) if isPrime[i]]

n = int(input())
numList = list(map(int,input().split()))

primeNumbers = getPrimes(max(numList))
totalMovement = 0
totalMax = 1

for v in primeNumbers:
    totalCount = 0
    powCount = []

    for num in numList:
        count = 0
        while num and num % v == 0:
            count += 1
            num //= v
        powCount.append(count)

    avg = sum(powCount) // n

    totalMax *= pow(v, avg)  # v^avg만큼 취할수있음

    for value in powCount:
        totalMovement += avg - value if avg > value else 0 #이동이 필요한 경우

print(totalMax,totalMovement)