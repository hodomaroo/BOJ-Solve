n = int(input())
nums = list(map(int,input().split()))
total = sum(nums)

ans = 0
for n in nums:
    ans += (n * (total - n))
print(ans//2)