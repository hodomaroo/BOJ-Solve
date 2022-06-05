nums = sorted([int(input()) for _ in range(int(input()))], reverse=True)
numSet = set(nums)
plusSet = {nums[i] + nums[j] for i in range(len(nums)) for j in range(i, len(nums))}

for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] - nums[j] in plusSet:
            print(nums[i])
            exit()