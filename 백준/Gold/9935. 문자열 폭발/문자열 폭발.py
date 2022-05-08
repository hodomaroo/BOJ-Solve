string = input().rstrip()
bomb = input().rstrip()


stack = []
res = []

for s in string:
    if stack and bomb[stack[-1]] == s:
        stack.append(stack[-1] + 1) #같은 경우 새로 추가
    else:
        stack.append(bomb[0] == s)
    res.append(s)

    if stack[-1] == len(bomb): #문자열 완성
        for i in range(len(bomb)):
            stack.pop()
            res.pop()

print(*res if res else "FRULA",sep="")


