n = int(input())
flowers = []

for _ in range(n):
    inform = list(map(int, input().split()))
    inform[:2] = max([3, 1], inform[:2])
    inform[2:] = min([11, 31], inform[2:])
    flowers.append(inform)

flowers.sort()
stack = []


for data in flowers:
    #구간을 이을 수 없는 경우 즉시 종료

    if stack and stack[-1][2:] < data[:2]:
        print(0)
        exit()

    if not stack or stack[-1][2:] < data[2:]: #구간 확장이 가능한 경우
        #치환 가능한 구간을 제거 (구간 시작은 동일하고 폭이 더 넓은경우 이전 구간 치환 가능)
        while stack and stack[-1][:2] >= data[:2] and stack[-1][2:] <= data[2:]:
            stack.pop()

        stack.append(data if not stack else (stack[-1][2:] + data[2:]))

ans = len(stack)
#print(stack)
print(ans if stack[0][:2] == [3,1] and stack[-1][2:] == [11,31] else 0)