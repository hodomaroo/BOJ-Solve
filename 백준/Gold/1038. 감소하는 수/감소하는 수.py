n = int(input())
stack = []
case = -2
def generate(last : int, depth : int):

    global case

    if depth == 10:
        case += 1
        #print(stack)
        if case == n:
            print(*stack, sep="")
            exit()
        return

    for i in range(10 - depth - 1 - (last == 10), last):  # 10 - depth - 2 -> Non Select
        if i != 10 - depth - 2:
            stack.append(i)

        #print(depth,stack)
        generate(10 if i == 10 - depth - 2 else i, depth + 1)

        if i != 10 - depth - 2:
            stack.pop()

generate(10,0)
print(-1)