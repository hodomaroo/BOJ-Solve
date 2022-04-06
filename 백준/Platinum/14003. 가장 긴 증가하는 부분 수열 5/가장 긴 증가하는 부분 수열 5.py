from bisect import bisect_left,bisect_right

n = int(input())
numList = list(map(int,input().split()))
stack = []
dp = [0] * n

for i in range(len(numList)):
    v = numList[i]
    position = bisect_left(stack, v)  # v의 위치 찾기
    dp[i] = position

    if position == len(stack):  #길이 추가
        stack.append(v)

    else:
        stack[position] = v

reveredStack = []
searchIndex = len(stack)-1

for i in range(n-1,-1,-1):
    if searchIndex == dp[i]:
        reveredStack.append(numList[i])
        searchIndex -= 1

print(len(reveredStack))
print(*reveredStack[::-1])