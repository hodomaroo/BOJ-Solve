_, nNums = int(input()), set(map(int, input().split()))
_, mNums = int(input()), list(map(int, input().split()))

for v in mNums:
    print(int(v in nNums))
