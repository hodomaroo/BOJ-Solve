n,m = map(int,input().split())
stack = []
for v in list(map(int,list(input()))):
    while stack and stack[-1] < v and m:
        stack.pop()
        m -= 1
    stack.append(v)
if not m:
    print(*stack ,sep="")
else:
    print(*stack[:-m], sep="")
