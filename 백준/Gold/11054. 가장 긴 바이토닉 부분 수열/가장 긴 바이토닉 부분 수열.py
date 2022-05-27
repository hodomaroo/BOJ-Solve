n = int(input())
nums = list(map(int,input().split()))

prefixDp = [1] * n
suffixDp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            prefixDp[i] = max(prefixDp[i], prefixDp[j] + 1)

        if nums[-i - 1] > nums[-j - 1]:
            suffixDp[-i - 1] = max(suffixDp[-i - 1], suffixDp[-j - 1] + 1)

for i in range(1,n):
    prefixDp[i] = max(prefixDp[i - 1], prefixDp[i])
    suffixDp[-i - 1] = max(suffixDp[-i - 1], suffixDp[-i])

prefixDp = [0] + prefixDp + [0]
suffixDp = [0] + suffixDp + [0]

maxLength = 1

for i in range(n + 1):
    maxLength = max(prefixDp[i] + suffixDp[i] - 1, maxLength)
print(maxLength)

