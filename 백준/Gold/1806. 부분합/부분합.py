#Two Pointer
n,m = map(int,input().split())
numbers = list(map(int,input().split()))

l,r = 0,0
total = 0
minDiff = float("inf")

while l < len(numbers):
    while r < len(numbers) and total < m:
        total += numbers[r]
        r += 1
        #r을 포함하지 않고, r - l개

    if total >= m:
        minDiff = min(minDiff, r - l)

    total -= numbers[l]
    l += 1
print(minDiff if minDiff != float("inf") else 0)