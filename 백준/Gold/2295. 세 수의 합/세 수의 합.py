nums = sorted([int(input()) for _ in range(int(input()))], reverse=True)
numSet = set(nums)
ans = 0
plusSet = {nums[i] + nums[j] for i in range(len(nums)) for j in range(i, len(nums))}
minusSet = {nums[j] - nums[i] for i in range(len(nums)) for j in range(i+1)}
multiSet = plusSet & minusSet

ans = 0
#print(plusSet,minusSet)
for v in nums: #maximum 1000
    for twoSum in multiSet:
        if v - twoSum in numSet:
            print(v)
            exit()