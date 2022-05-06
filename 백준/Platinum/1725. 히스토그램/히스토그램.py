import sys

input = sys.stdin.readline

stack = [0]
maxArea = 0
n = int(input())
height = [0] + [int(input()) for _ in range(n)] + [0]

for i in range(1,n+2):    #한번 더 진행함
    while height[stack[-1]] > height[i]:
        cur_i = stack.pop()
        maxArea = max((i - stack[-1] - 1) * height[cur_i],maxArea)
    stack.append(i)
print(maxArea)
