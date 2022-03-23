from math import sqrt

n = int(input())
dpSet = {0}
count = 0

while True:
    count += 1

    nextdpSet = dpSet.copy()
    for v in dpSet:
        for pv in range(1,int(sqrt(n))+1):
            if v + (pv * pv) > n: break
            nextdpSet.add(v + pv * pv)
    dpSet = nextdpSet | dpSet

    if n in dpSet:
        print(count)
        break
