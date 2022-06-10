from functools import cmp_to_key

def compare(a : str, b : str) -> int:
    return [-1, 1][a + b < b + a]

n = int(input())
nums = input().split()
nums.sort(key=cmp_to_key(compare))

print("".join(nums) if nums[0] != "0" else 0)

