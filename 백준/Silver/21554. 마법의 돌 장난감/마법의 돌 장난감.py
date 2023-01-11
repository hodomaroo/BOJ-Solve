n = int(input())
nums = list(map(int,input().split()))

log = []

for i in range(1, n + 1):
    l,r = i - 1, nums.index(i)
    if l != r:
        nums = nums[:l] + nums[l:r + 1][::-1] + nums[r + 1:]
        log.append([l + 1,r + 1])

print(len(log))
for _ in log:
    print(*_)
